import subprocess
import json

class Function:
    port = 7001
    def __init__(self, image, trigger_value):
        self.image = image
        self.trigger_value = trigger_value
        self.port = str(Function.port)
        Function.port += 1
    def __str__(self):
        return json.dumps(self.__dict__)
    
def write_to_json(mapping):
    serialized = json.dumps(mapping, default=lambda o: o.__dict__)
    with open("mapping.json", "w") as f:
        f.write(serialized)


print("Welcome to FaaSiNetes")
mapping = {"COOLDOWN":300}

while True:

    try:
        print()
        print('==='*30)
        print("Enter:\n1 to Register a function, \n2 to Register a Trigger, \n3 to List Functions and Triggers, \n4 To stop a function \n5 to change cooldown period \n6 to exit")
        print('==='*30)
        print()

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
            if function_name not in mapping:
                print("Function not found")
                continue
            print("Enter the trigger name: 1. HTTP, 2. CronJob")
            trigger_name = int(input())
            if trigger_name == 1:
                mapping[function_name].trigger_value = "HTTP"
                write_to_json(mapping)
                print("HTTP Trigger registered successfully")
                print("Trigger using: http://localhost:5000/trigger/"+function_name)

            elif trigger_name == 2:
                print("Enter frequency in min")
                cron_time = int(input())
                cooldown = mapping["COOLDOWN"] # already in seconds
                cron_expression = str(cron_time) + " * * * *"
                mapping[function_name].trigger_value = cron_expression
                cport = mapping[function_name].port
                write_to_json(mapping)
                subprocess.run(["bash", "create_cronjob.sh", cron_expression, function_name, image_name, cport , str(cooldown)]) 
                print("CronJob created successfully") 
            else:
                print("Invalid Trigger")
        elif choice == 3:
            print("Registered Functions and Triggers")
            for key, value in mapping.items():
                if key == "COOLDOWN":
                    print("Cooldown period: ", value)   
                else:
                    print(key, str(value))
        elif choice == 4:
            print("Enter function name to stop")
            function_name = input()
            if function_name not in mapping:
                print("Function not found")
            else:
                del mapping[function_name]
                write_to_json(mapping)
            # crontab -l | grep -v out$2.log  | crontab -
            subprocess.run(["bash", "delete_function.sh", str(1), function_name])
        elif choice == 5:
            print("Enter cooldown period in min")
            cooldown = int(input())
            mapping["COOLDOWN"] = cooldown*60
            write_to_json(mapping)
            print("Cooldown period updated successfully")
        elif choice == 6:
            break
               


    except Exception as e:
        print(e)
        continue
          
    