from alfred.config import data_settings, input_settings, secrets

# Use the variables in your code
print("----printing secrets----")
print(f"API Key: {secrets.api_key}")
print(f"Database URL: {secrets.database_url}")

print("----printing configs----")
print(data_settings.data_file)
print(data_settings.data_columns)
print(input_settings.input_size)
print(input_settings.batch_size)
