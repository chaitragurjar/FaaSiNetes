echo "Enter type of trigger: 1. Timer trigger, 2. HTTP trigger 3. Event trigger"
read trigger_type
echo "Trigger type is $trigger_type"
if [ $trigger_type -eq 1 ]
then
    echo "Enter the cron expression"
    read cron_expression
    echo "Cron expression is $cron_expression"
elif [ $trigger_type -eq 2 ]
then
    http_endpoint="http://localhost:7000"
    echo "HTTP endpoint is $http_endpoint"
elif [ $trigger_type -eq 3 ]
then
    echo "Enter the event type"
    read event_type
    echo "Event type is $event_type"
else
    echo "Invalid trigger type"
fi