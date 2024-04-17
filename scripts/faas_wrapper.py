import subprocess

class Trigger:
    def __init__(self, name, trigger_value):
        self.name = name
        self.trigger_value = trigger_value


mapping = {}



print("Enter 1 to Register a function, 2 to Register a Trigger, 3 to List Functions and Triggers")

choice = int(input())
if choice == 1:
    print("Enter the image name")
    image_name = input()
    mapping[image_name] = None
elif choice == 2:
    print("Enter the image name")
    image_name = input()
    print("Enter the trigger name: 1. HTTP, 2. CronJob")
    trigger_name = input()
    if trigger_name == 1:
        pass
    elif trigger_name == 2:
        print("Enter the cron expression")
        cron_expression = input()
        mapping[image_name] = Trigger("CronJob", cron_expression)
        subprocess.run(["bash", "scripts/register_cronjob.sh", cron_expression, image_name])        
    else:
        print("Invalid Trigger")