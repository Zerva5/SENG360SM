from dataclasses import dataclass
import datetime
from Account import Account
from Message import Message


@dataclass    
class Chat:
    sender: Account
    recipient: Account

    IP: str = dataclass.field(init=False)
    sessionKey: str = dataclass.field(init=False) # Not 100% if its one key or two.
    messages: list[Message] = []# list is the same as an array

    def __post_init__(self):
        """
        DOn't think anything should go here for now, but adding it because I dind't know it was a thing and it may be useful

        Maybe print out messages from last connection with this person?
        """
        return
        
    def Connect(self) -> bool:
        """
        Connect to IP
        Request a chat
         - Verify identity of other user
         - Perform some form of key exchange (https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) for example.
        Return once connection is established, identify verified, and keys exchanged
        """
        return False

    def Send(self, message: Message):
        """
        Encrypt and send the message.
        Format message to have the message hash and timestamp
        """
        return

    def Receive(self) -> Message:
        """
        Check for recieved messages and decrpyt them.
        Also decode them, verify message integrity using message hash and timestamp
        Raise exception if message can't be decrypted or can't be verified by message hash
        """


        return Message("", datetime.datetime.now(), Account("", ""), Account("", ""))

    def SaveHistory(self):
        """
        Save the contents of "messages" to a file and encrypt it
        """

        return

    def PrintMessage(self, msg: Message):
        """
        Format and print the message
        ex 10:35 - Lucas: Hey guys this is a message

        Don't care what format thats just an example
        """

        return
        
        
