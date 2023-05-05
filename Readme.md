# conky.twitter.py
This is a Python code snippet that utilizes the `Tweepy` library to interact with the `Twitter API`. The code authenticates the Twitter API using the `consumer key`, `consumer secret`, `access token`, and `access token secret`. It then retrieves the most recent 5 notifications or mentions of the authenticated user's Twitter account using the `mentions_timeline()` method.

The retrieved notifications are then formatted using the Conky system monitor format and stored in the output variable. Finally, the formatted notifications are printed to the console using the print() function.

## Usage
To use this code, you will need to have a Twitter account and have access to the Twitter API. Follow these steps to use the code:

1. Create a Twitter Developer account and apply for a developer account to obtain the necessary credentials to access the Twitter API. You can follow the instructions on the Twitter Developer documentation page to create your account and obtain your credentials.
2. Install the Tweepy library in your Python environment. You can install Tweepy using the pip package manager by running the following command in your terminal or command prompt:

```Bash
pip install tweepy
```

3. Copy the code snippet you provided into a Python file (e.g., notifications.py), and replace the placeholder strings ('your_consumer_key', 'your_consumer_secret', 'your_access_token', 'your_access_token_secret') with your actual Twitter API credentials.
4. Save the file and run it using a Python interpreter (e.g., python notifications.py). The script will connect to the Twitter API, retrieve the most recent 5 notifications or mentions, and format them in the Conky format.

## Considerations
The user may want to modify the number of notifications retrieved by changing the count parameter in the `api.mentions_timeline()` method. For example, notifications = api.mentions_timeline(count=10) will retrieve the 10 most recent notifications instead of the default 5.

If the user wants to display the notifications in Conky, they may need to modify the formatting of the output string to match their desired display format. They can also modify the font, color, and positioning of the notification text by changing the values passed to the Conky format tags (e.g., `${font Source Code Pro:size=10}` and `${color #4F4F4F}`).

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).
