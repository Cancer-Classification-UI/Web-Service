import gradio as gr
import logging

log = logging.getLogger('web-api')

def setup(acc_creation_col, login_col):
    """
    Setup the account creation interface

    Parameters:
    acc_creation_col (gradio.Column): The column to add the interface to
    login_col (gradio.Column): The column to switch to when the cancel button is clicked
    """
    with acc_creation_col:
        log.debug("Setting up account creation interface")
        gr.Markdown("<h1 style=\"text-align: center; font-size: 48px;\">Create Account</h1>")
        gr.Markdown("<p style=\"text-align: center;\">Create an account by filling in info below.</p>")
        user_email_txt = gr.Textbox(label="Email", interactive=True, max_lines=1, value=None)
        username_txt = gr.Textbox(label="Username", interactive=True, max_lines=1, value=None)
        passwd_txt = gr.Textbox(label="Password", interactive=True, max_lines=1, type="password", value=None)
        c_passwd_txt = gr.Textbox(label="Confirm Password", interactive=True, max_lines=1, type="password", value=None)
        sign_up_btn = gr.Button("Sign Up")

        cancel_btn = gr.Button("Cancel", elem_id="linkbutton", variant="secondary", size="sm",)
        cancel_btn.click(reset, outputs=[login_col, acc_creation_col, user_email_txt, username_txt, passwd_txt, c_passwd_txt])


def reset():
    """
    Resets the account creation page, and also all the inputs
    
    Returns:
    gradio.Column: The column responsible for login
    gradio.Column: The column responsible for account creation
    gradio.Textbox: The textbox responsible for the user's email
    gradio.Textbox: The textbox responsible for the user's username
    gradio.Textbox: The textbox responsible for the user's password
    gradio.Textbox: The textbox responsible for the user's password confirmation
    """
    return gr.update(visible=True), gr.update(visible=False), gr.update(value=None), gr.update(value=None), gr.update(value=None), gr.update(value=None)