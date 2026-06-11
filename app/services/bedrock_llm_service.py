from langchain_aws import ChatBedrock

def get_llm():

    return ChatBedrock(
        model_id="amazon.nova-pro-v1:0",
        region_name="us-east-1",
        model_kwargs={
            "maxTokens": 512,
            "temperature": 0.2,
        }
    )