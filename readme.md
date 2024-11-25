
# Email Attachment Downloader & Timestamp Resetter

  

This desktop application is designed to streamline the process of downloading email attachments from any mail account to a computer. Moreover, it resets the timestamp of the downloaded file to match the date and time of the email itself, ensuring accurate chronological organization of files based on their original email timestamps rather than the download time.

  

The application monitors the configured mail account and automatically downloads attachments when an email with an attachment arrives. It then adjusts the file's timestamp to match the timestamp of the email from which the attachment originated.

  

## Tools and Libraries

  

The project is built using Python, utilizing the following tools and libraries:

  

-  **filedate**: Python library for modifying file timestamps.

-  **imaplib**: Python library for accessing and manipulating mail accounts via IMAP.

-  **email**: Python library for managing email messages.

  

## Installation

  

To run the project, follow these steps:

  

1.  **Install Python**: If Python is not installed on your system, download and install it from the [official Python website](https://www.python.org/).

2.  **Install Dependencies**: Use pip to install the required dependencies by running the command:

`pip install -r requirements.txt`

  

3.  **Configure Account Credentials**: Set up the `config.json` file with the appropriate credentials for the mail account that will be monitored.

  

4.  **Run the Application**: Start the application by executing the following command:

`python main.py`

  

## How It Works

  

Once the app is launched and configured, it continuously monitors the specified mail account for incoming emails with attachments. When it detects an email with an attachment, it automatically downloads the attachment to the designated 'attachments' folder.

  

Upon downloading the attachment, the application retrieves the timestamp associated with the email and modifies the file's timestamp to match that specific email timestamp. This process ensures that the file's modified date and time align with the original email's timestamp.

  

The application simplifies the task of managing downloaded attachments, organizing them based on their original email timestamps rather than the time of download, thus maintaining a more accurate and meaningful chronological order.

  

**Note:** Make sure the application has the necessary permissions to access and modify files on your system.

  

## Demo

[![Watch demo](https://raw.githubusercontent.com/ShahrozAtiq/linkedin-mass-accounts-creator/master/play.webp)](https://dl.dropboxusercontent.com/scl/fi/0kqpg8bk5bxt27l2v9284/imap-downloader.mp4?rlkey=hm83a2db0xc5ctpj9bzkzgtec)


  

## Configuration

  

The `config.json` file should include the following fields:

  

-  `mail_credentials`: Specify the credentials required to access the mail account (e.g., `username`,`password`).

-  `attachment_folder`: Define the folder where attachments will be stored in `download_path`.

  

## Important Considerations

  

Ensure the mail account being used has appropriate permissions and settings to access and download attachments.

  

This application is intended to simplify the process of managing attachments. Use it responsibly and ensure it complies with the policies and regulations associated with accessing and handling email content.

  

## Support

  

For questions, feedback, or support, please contact 
<table>
  <tr>
    <td align="center">
      <a href="https://www.upwork.com/freelancers/~01c437b099d917194b" title="View my Upwork profile">
        <img src="https://img.icons8.com/external-tal-revivo-shadow-tal-revivo/48/null/external-upwork-a-global-freelancing-platform-where-professionals-connect-and-collaborate-remotely-logo-shadow-tal-revivo.png" alt="Upwork Icon" width="60" height="60"/>
      </a>
    </td>
    <td align="center">
      <a href="https://www.fiverr.com/shahrozatiq" title="View my Fiverr profile">
        <img src="https://ml.globenewswire.com/Resource/Download/dcc91863-eeb0-4879-a556-9f7608b19744" alt="Fiverr Icon" width="60" height="60"/>
      </a>
    </td>
    <td align="center">
      <a href="mailto:shahrozatiq123@gmail.com" title="Send me an email">
        <img src="https://www.svgrepo.com/show/452213/gmail.svg" alt="Gmail Icon" height="60" width="60"/>
      </a>
    </td>
    <td align="center">
      <a href="https://wa.me/923014317809" title="Chat with me on WhatsApp">
        <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/whatsapp.svg" alt="WhatsApp Icon" height="60" width="60"/>
      </a>
    </td>
    <td align="center">
      <a href="https://linkedin.com/in/shahroz-atiq" title="Connect with me on LinkedIn">
        <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn Icon" height="60" width="60"/>
      </a>
    </td>
    <td align="center">
      <a href="https://instagram.com/shahahahahroz" title="Follow me on Instagram">
        <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram Icon" height="60" width="60"/>
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://www.upwork.com/freelancers/~01c437b099d917194b">Upwork</a>
    </td>
    <td align="center">
      <a href="https://www.fiverr.com/shahrozatiq">Fiverr</a>
    </td>
    <td align="center">
      <a href="mailto:shahrozatiq123@gmail.com">Gmail<br>shahrozatiq123@gmail.com</a>
    </td>
    <td align="center">
      <a href="https://wa.me/923014317809">WhatsApp<br>+923014317809</a>
    </td>
    <td align="center">
      <a href="https://linkedin.com/in/shahroz-atiq">LinkedIn</a>
    </td>
    <td align="center">
      <a href="https://instagram.com/shahahahahroz">Instagram</a>
    </td>
  </tr>
</table>

