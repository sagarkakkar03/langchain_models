from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI(model='gpt-5.2')

class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review."]
    summary: Annotated[str, "A brief summary of the review."] 
    sentiment: Annotated[Literal['Positive', 'Negative', 'Nuetral'], "Return sentiment of the review strictly out of negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros in the form of the list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons in the form of the list"]
    name: Annotated[Optional[str], "Write the name of the reviewer."] 

model = model.with_structured_output(Review)

result = model.invoke("""I met a traveller from an antique land
Who said: \"Two vast and trunkless legs of stone
Stand in the desert . . . Near them, on the sand,
Half sunk, a shattered visage lies, whose frown,
And wrinkled lip, and sneer of cold command,
Tell that its sculptor well those passions read
Which yet survive, stamped on these lifeless things,
The hand that mocked them, and the heart that fed:
And on the pedestal these words appear:
My name is Ozymandias, king of kings:
Look on my works, ye Mighty, and despair!
Nothing beside remains. Round the decay
Of that colossal wreck, boundless and bare
The lone and level sands stretch far away.\”
""")
print(result)