import boto3
import pickle
import json

# Creating the low level functional client
client = boto3.client(
    's3',
    aws_access_key_id='abc',
    aws_secret_access_key='xyz',
    region_name='us-east-1'
)


# Fetch the list of existing buckets
clientResponse = client.list_buckets()

# Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')


myData = {"backend_name": "qasm_simulator", "backend_version": "2.0.0", "qobj_id": "77fa4452-239e-4304-8c63-04c2cd828bfd", "job_id": "35d36c6e-ab07-4d52-a769-14f3168a967a", "success": "true", "results": [{"shots": 1024, "success": "true", "data": {"counts": {"0x3": 530, "0x0": 494}}, "meas_level": 2, "header": {"qubit_labels": [["q", 0], ["q", 1]], "n_qubits": 2, "qreg_sizes": [["q", 2]], "clbit_labels": [["c", 0], ["c", 1]], "memory_slots": 2, "creg_sizes": [["c", 2]], "name": "circuit7", "global_phase": 0.0}, "status": "DONE", "name": "circuit7", "seed_simulator": 1051128335, "time_taken": 0.01583695411682129}], "status": "COMPLETED", "header": {}, "time_taken": 0.01583695411682129}
serializedMyData = json.dumps(myData)

client.put_object(Bucket='srihithas3bucket',Key='dict1',Body=serializedMyData)

object = client.get_object(Bucket='srihithas3bucket',Key='dict1')
serializedObject = object['Body'].read()

myData = json.loads(serializedObject)

print(myData)