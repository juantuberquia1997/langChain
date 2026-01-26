from langchain_community.document_loaders import PlaywrightURLLoader

loader = PlaywrightURLLoader(
    urls=["https://astro.build/"],
		headless=True,
)

docs = loader.load()
print("infopage", docs)