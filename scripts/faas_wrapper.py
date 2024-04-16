import subprocess

class Function:
    def __init__(self, name, image_name, trigger, trigger_value):
        self.name = name
        self.image_name = image_name
        self.trigger = trigger
        self.trigger_value = trigger_value


function_trigger_mapping = {}


print("Enter 1 to Register a function, 2 to Register a Trigger, 3 to List Functions and Triggers")

choice = int(input())
if choice == 1:
    print("Enter the image name")
    image_name = input()
    function_trigger_mapping[image_name] = None
elif choice == 2:
    print("Enter the trigger name: 1. HTTP, 2. CronJob")
    trigger_name = input()
    if trigger_name == 1:
        pass
    elif trigger_name == 2:
        print("Enter the cron expression")
        cron_expression = input()
        subprocess.run(["bash", "scripts/register_cronjob.sh", cron_expression, image_name])        
    else:
        print("Invalid Trigger")