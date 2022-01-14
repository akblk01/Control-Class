import random
import msvcrt

class Control():

    def __init__(self,tv_status = "Close",tv_sound = 0,channel_list = ["Trt"],channel = "Trt"):
        print("The controller is being created.")

        self.tv_sound =  tv_sound

        self.tv_status = tv_status

        self.channel_list =channel_list

        self.channel = channel
    def volume_adjustment(self):

        while True:
            character = input("Press '>' to increase, '<' to decrease, 'q' if OK")

            if (character == "<"):
                if (self.tv_sound != 0):
                    self.tv_sound -= 1
                    print("Sound:",self.tv_sound)
            elif (character == ">"):
                if (self.tv_sound != 32):
                    self.tv_sound += 1
                    print("Sound:",self.tv_sound)
            else:
                print("Sound Updated:",self.tv_sound)
                break
    def turn_off_tv(self):
        print("TV turns off.")

        self.tv_status = "Close"
    def turn_on_tv(self):
        print("TV turns on.")
        self.tv_status = "Open"
    def __str__(self):
        return "Tv Status : {}\nSound: {}\nChannels: {}\nCurrent channel: {}\n".format(self.tv_status,self.tv_sound,self.channel_list,self.channel)
    def __len__(self):
        return  len(self.channel_list)

    def random_channel(self):
        random1 = random.randint(0,len(self.channel_list)-1)

        self.channel = self.channel_list[random1]

        print("Current channel:", self.channel)
    def channel_add(self,channel):
        print("Channel added ",channel)
        self.channel_list.append(channel)


control = Control()
print("""*******************

Television Application

Transactions ;

1. Turn On the TV

2. Turn off the TV

3. Television Information

4. Learning the Number of Channels

5. Add Channel

6. Switch to Random Channel

7. Decrease or Increase the Volume
Press 'q' to exit..
*******************""")

while True:

    transaction = input("Select Transaction:")
    if (transaction == "q"):
        print("Exiting Program...")
        break
    if (transaction == "1"):
        control.turn_on_tv()
    elif (transaction == "2"):
        control.turn_off_tv()
    elif (transaction == "3"):
        print(control)
    elif (transaction == "4"):
        print("Number of Channels: ",len(control))
    elif (transaction == "5"):
        channels = input("Enter the Channels you want to add, separated by ',':")
        will_be_added = channels.split(",")
        for i in will_be_added:

            control.channel_add(i)
        print("Channel List Updated Successfully.")
    elif (transaction == "6"):
        control.random_channel()
    elif (transaction == "7"):
        control.volume_adjustment()
    else:
        print("Invalid Operation...")











