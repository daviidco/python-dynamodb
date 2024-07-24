import boto3

# Configura el cliente de DynamoDB para apuntar al endpoint local
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url="http://localhost:8000",
    aws_access_key_id="fakeMyKeyId",
    aws_secret_access_key="fakeSecretAccessKey",
    region_name="us-west-2"
)

# Crear una tabla en DynamoDB Local
def create_table():
    table = dynamodb.create_table(
        TableName='DemoTable',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Clave primaria
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.wait_until_exists()
    print(f"Tabla creada: {table.table_name}")

# Lista las tablas existentes
def list_tables():
    tables = list(dynamodb.tables.all())
    print("Tablas en DynamoDB Local:", tables)

# Añadir un ítem a la tabla
def add_item():
    table = dynamodb.Table('DemoTable')
    table.put_item(
        Item={
            'id': '1',
            'name': 'John Doe',
            'age': 30
        }
    )
    print("Ítem añadido a la tabla.")

# Eliminar una tabla
def delete_table(table_name: str):
    table = dynamodb.Table(table_name)
    table.delete()
    table.wait_until_not_exists()
    print(f"Tabla eliminada: {table.table_name}")

if __name__ == "__main__":
    create_table()
    list_tables()
    add_item()
    list_tables()
    # delete_table('DemoTable')
