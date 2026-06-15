from langchain_aws import ChatBedrock

def get_llm():

    print("===== USING BEDROCK =====")
    print("MODEL: amazon.nova-lite-v1:0")
    print("REGION: us-east-1")

    return ChatBedrock(
        model_id="amazon.nova-lite-v1:0",
        region_name="us-east-1",
        model_kwargs={
            "maxTokens": 512,
            "temperature": 0.2,
        }
    )