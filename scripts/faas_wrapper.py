import subprocess

class Function:
    port = 7001
    def __init__(self, image, trigger_value):
        self.image = image
        self.trigger_value = trigger_value
        self.port = str(Function.port)
        Function.port += 1

mapping = {}

while True:

    try:
        print("Enter 1 to Register a function, 2 to Register a Trigger, 3 to List Functions and Triggers, 4 To stop a function")

        choice = int(input())
        if choice == 1:
            print("Enter the function name")
            function_name = input()
            print("Enter the image name")
            image_name = input()
            mapping[function_name] = Function(image_name, None)
        elif choice == 2:
            print("Enter the function name")
            function_name = input()
            print("Enter the trigger name: 1. HTTP, 2. CronJob")
            trigger_name = int(input())
            if trigger_name == 1:
                pass
            elif trigger_name == 2:
                print("Enter frequency in min & cooldown period in min")
                cron_time, cooldown  = map(int, input().split())
                cron_expression = str(cron_time) + " * * * *"
                mapping[function_name].trigger_value = cron_expression
                cport = mapping[function_name].port
                subprocess.run(["bash", "create_cronjob.sh", cron_expression, function_name, image_name, cport , str(cooldown*60)]) 
                print("CronJob created successfully") 
            else:
                print("Invalid Trigger")
        elif choice == 3:
            print("Registered Functions and Triggers")
            for key, value in mapping.items():
                print(key, value.trigger_value)
        elif choice == 4:
            # remove cronjob
            print("Enter function name to stop")
            function_name = input()
            if function_name not in mapping:
                print("Function not found")
            else:
                del mapping[function_name]
            # crontab -l | grep -v out$2.log  | crontab -
            subprocess.run(["bash", "cooldown.sh", str(1), function_name])


    finally:
        continue  
    