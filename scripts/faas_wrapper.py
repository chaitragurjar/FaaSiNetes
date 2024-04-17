import subprocess

class Function:
    def __init__(self, image, trigger_value):
        self.image = image
        self.trigger_value = trigger_value


mapping = {}


while True:
        
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
            print("Enter the cron expression")
            cron_expression = input()
            # try to save later
            mapping[function_name].trigger_value = cron_expression
            subprocess.run(["bash", "create_cronjob.sh", cron_expression, function_name, image_name]) 
            print("CronJob created successfully")       
        else:
            print("Invalid Trigger")
    elif choice == 3:
        print("Registered Functions and Triggers")
        for key, value in mapping.items():
            print(key, value.name, value.trigger_value)
    elif choice == 4:
        # remove cronjob
        print("Enter function name to stop")
        function_name = input()
        if function_name not in mapping:
            print("Function not found")
            continue
        del mapping[function_name]
        subprocess.run(["bash", "delete_function.sh", function_name])
        subprocess.run(["crontab", "-r"])
