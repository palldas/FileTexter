# iMessageSender

The iMessage Sender is a Python script that allows you to send text messages (iMessages) to a specified phone number using the macOS Messages app. It reads the messages from a text file and sends them as iMessages. (**Note**: this will only work if you have texted the number previously on Messages.)

### Setup:
Before using this script, ensure you have the following:

1. Python 3 installed with pip package manager
2. MacOS operating system
3. Apple Messages app configured with your iMessage account
4. Install the required python libraries with `pip install applescript`

## Usage

### Command-line Arguments
The script uses command-line arguments to control its behavior. Below are the available arguments:

- `filename`: The name of the text file containing the messages to be sent
- `number`: The phone number to which the messages will be sent
- `-t`: An optional argument to set the time delay (in seconds) between sending messages. The default value is 1.75 seconds
- `--byline`: An optional flag. If present, it indicates that each line in the file represents a separate message. If not present, each word in a line will be sent as separate messages

### Sending Messages
1. Run the script with `python3 send_msgs.py your_message_file.txt 1234567890`
    1. To use the byline arg, run `python3 send_msgs.py --byline your_message_file.txt 1234567890`
    2. To change the time delay arg from 1.75s, run `python3 send_msgs.pyp -t 3 your_message_file.txt`. This example changes the delay to 3 seconds.

The script will start sending the messages to the specified phone number via iMessage from your phone number. It will wait for the specified time delay between sending each message.