import boto3

# Setting the DynamoDB client to point to the local endpoint
dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url="http://localhost:8000",
    aws_access_key_id="fakeMyKeyId",
    aws_secret_access_key="fakeSecretAccessKey",
    region_name="us-west-2"
)


def create_table():
    """
    Create a DynamoDB with a partition key 'id'.
    """
    table = dynamodb.create_table(
        TableName='DemoTable',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
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
    print(f"Created table: {table.table_name}")


def list_tables():
    """
    List all tables in the local DynamoDB instance.

    Prints the names of all tables available in the local DynamoDB.
    """
    tables = list(dynamodb.tables.all())
    print("Tables at Local DynamoDB:", tables)


def add_item():
    """
    Add an item to the 'DemoTable' in DynamoDB.

    The item added has an 'id' of '1', a 'name' of 'John Doe', and an 'age' of 30.
    Prints a confirmation message after adding the item.
    """
    table = dynamodb.Table('DemoTable')
    table.put_item(
        Item={
            'id': '1',
            'name': 'John Doe',
            'age': 30
        }
    )
    print("Item added to table")


def delete_table(table_name: str):
    """
    Delete a DynamoDB table by name.

    Args:
        table_name (str): The name of the table to delete.

    Waits until the table no longer exists before printing a confirmation message.
    """
    table = dynamodb.Table(table_name)
    table.delete()
    table.wait_until_not_exists()
    print(f"Deleted table: {table.table_name}")


if __name__ == "__main__":
    create_table()
    list_tables()
    add_item()
    list_tables()
    # delete_table('DemoTable')
