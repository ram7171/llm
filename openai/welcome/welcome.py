import os
from langchain_openai import OpenAI

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
load_dotenv()
print("hello world")

def main():
    print("This is the main function.")
    print(os.environ.get("OPENAI_API_KEY"))
    # message = """
    # Elon Reeve Musk FRS (/ˈiːlɒn/ EE-lon; born June 28, 1971) is an international businessman and entrepreneur known for his leadership of Tesla, SpaceX, X (formerly Twitter), and the Department of Government Efficiency (DOGE). Musk has been the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion.
    # Born to a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he had obtained Canadian citizenship at birth through his Canadian-born mother. He received bachelor's degrees in 1997 from the University of Pennsylvania in Philadelphia, United States, before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became an American citizen.
    # In 2002, Musk founded the space technology company SpaceX, becoming its CEO and chief engineer; the company has since led innovations in reusable rockets and commercial spaceflight. Musk joined the automaker Tesla as an early investor in 2004 and became its CEO and product architect in 2008; it has since become a leader in electric vehicles. In 2015, he co-founded OpenAI to advance artificial intelligence (AI) research but later left; growing discontent with the organization's direction and their leadership in the AI boom in the 2020s led him to establish xAI. In 2022, he acquired the social network Twitter, implementing significant changes and rebranding it as X in 2023. His other businesses include the neurotechnology company Neuralink, which he co-founded in 2016, and the tunneling company the Boring Company, which he founded in 2017.
    # """
    #
    # summary_template = """"
    # Given the information about a person {message},
    #  provide a concise summary of their key achievements and background in no more than 100 words.
    # """
    #
    # summary_prompt_tempate = PromptTemplate(
    #     input_variables=["message"],
    #     template=summary_template)
    #
    # llm = ChatOpenAI(temperature=0, model="gpt-5")
    # chain = summary_prompt_tempate | llm
    # response = chain.invoke(input={"information": message})
    # print(response)
    llm = OpenAI(temperature=0.9)
    print(llm.invoke("What would be a good company name for a company that makes colorful socks?"))


if __name__ == "__main__":
    main()