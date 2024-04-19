# flask app
from flask import Flask, request, jsonify
import subprocess
import os
import json

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return "Welcome to FaaSiNetes"

@app.route('/trigger/<functionname>', methods=['GET'])
def trigger(functionname):
    # subprocess.run(["bash", "trigger_dispatch.sh", functionname])
    # load mapping.json
    with open("mapping.json", "r") as f:
        mapping = json.load(f)
    # do this
    image = mapping[functionname]['image']
    port = mapping[functionname]['port']
    cooldown = mapping['COOLDOWN']
    os.system("bash trigger_dispatch.sh "+functionname+" "+image+" "+port+" "+str(cooldown)+" >> out"+functionname+".log 2>&1 & " )
    # /bin/bash $(pwd)/trigger_dispatch.sh $2 $3 $4 $5>> $(pwd)/out$2.log 2>&1" )
    if functionname in mapping:
        print("Function found")
        print(mapping[functionname]['image'])
        print(mapping[functionname]['port'])
    return mapping[functionname]
    # trigger dispatch.sh to be called


if __name__ == '__main__':
    app.run()