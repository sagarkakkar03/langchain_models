import json
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal

schema = json.loads(Path("json_schema.json").read_text(encoding="utf-8"))
print(schema)
load_dotenv()

# class Review(BaseModel):
#     key_themes: list[str] = Field(description='Write down all the key themes discussed in the review.')
#     summary: str = Field(description="A brief summary of the review.")
#     sentiment: Literal['Positive', 'Negative', 'Nuetral'] =  Field(description="Return sentiment of the review strictly out of negative, positive or neutral")
#     pros: Optional[list[str]] = Field(description="Write down all the pros in the form of the list")
#     cons: Optional[list[str]] = Field(description="Write down all the cons in the form of the list")
#     name: Optional[str] = Field(description="Write the name of the reviewer.")

model = ChatOpenAI(model='gpt-5')

model = model.with_structured_output(schema)

print(model.invoke("""I met a traveller from an antique land
Who said: Two vast and trunkless legs of stone
Stand in the desert . . . Near them, on the sand,
Half sunk, a shattered visage lies, whose frown,
And wrinkled lip, and sneer of cold command,
Tell that its sculptor well those passions read
Which yet survive, stamped on these lifeless things,
The hand that mocked them, and the heart that fed:
And on the pedestal these words appear:‘My name is Ozymandias, king of kings:
Look on my works, ye Mighty, and despair!
Nothing beside remains. Round the decay
Of that colossal wreck, boundless and bare
The lone and level sands stretch far away."""))