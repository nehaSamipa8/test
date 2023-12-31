
import importlib
from typing import Any


def import_class(class_path):
    module_name, class_name = class_path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

def document_loader(reader_type: str) -> Any:
    mapping = {
                "airtable": "openagent.knowledgebase.document_loaders.airtable.base.AirtableReader",
                "apify_dataset": "openagent.knowledgebase.document_loaders.apify.dataset.base.ApifyDataset",
                "asana": "openagent.knowledgebase.document_loaders.asana.base.AsanaReader",
                "azcognitive_search": "openagent.knowledgebase.document_loaders.azcognitive_search.base.AzCognitiveSearchReader",
                "bilibili": "openagent.knowledgebase.document_loaders.bilibili.base.BilibiliTranscriptReader",
                "boarddocs": "openagent.knowledgebase.document_loaders.boarddocs.base.BoardDocsReader",
                "chatgpt_plugin": "openagent.knowledgebase.document_loaders.chatgpt_plugin.base.ChatGPTRetrievalPluginReader",
                "chroma": "openagent.knowledgebase.document_loaders.chroma.base.ChromaReader",
                "confluence": "openagent.knowledgebase.document_loaders.confluence.base.ConfluenceReader",
                "couchdb": "openagent.knowledgebase.document_loaders.couchdb.base.SimpleCouchDBReader",
                "dad_jokes": "openagent.knowledgebase.document_loaders.dad_jokes.base.DadJokesReader",
                "deep_lake": "openagent.knowledgebase.document_loaders.deeplake.base.DeepLakeReader",
                "discord": "openagent.knowledgebase.document_loaders.discord.base.DiscordReader",
                "docugami": "openagent.knowledgebase.document_loaders.docugami.base.DocugamiReader",
                "elasticsearch": "openagent.knowledgebase.document_loaders.elasticsearch.base.ElasticsearchReader",
                "faiss": "openagent.knowledgebase.document_loaders.faiss.base.FaissReader",
                "feedly_rss": "openagent.knowledgebase.document_loaders.feedly_rss.base.FeedlyRssReader",
                "feishu_docs": "openagent.knowledgebase.document_loaders.feishu_docs.base.FeishuDocsReader",
                "file_directory": "openagent.knowledgebase.document_loaders.file.base.SimpleDirectoryReader",
                "file_audio": "openagent.knowledgebase.document_loaders.file.audio.base.AudioTranscriber",
                "gladia_audio": "openagent.knowledgebase.document_loaders.file.audio_gladia.base.GladiaAudioTranscriber",
                "file_cjk_pdf": "openagent.knowledgebase.document_loaders.file.cjk_pdf.base.CJKPDFReader",
                "deep_doctection": "openagent.knowledgebase.document_loaders.file.deepdoctection.base.DeepDoctectionReader",
                "file_docx": "openagent.knowledgebase.document_loaders.file.docx.base.DocxReader",
                "file_epub": "openagent.knowledgebase.document_loaders.file.epub.base.EpubReader",
                "flat_pdf": "openagent.knowledgebase.document_loaders.file.flat_pdf.base.FlatPdfReader",
                "image": "openagent.knowledgebase.document_loaders.file.image.base.ImageReader",
                "image_caption": "openagent.knowledgebase.document_loaders.file.image_blip.base.ImageCaptionReader",
                "image_vision": "openagent.knowledgebase.document_loaders.file.image_blip2.base.ImageVisionLLMReader",
                "image_tabular_chart": "openagent.knowledgebase.document_loaders.file.image_deplot.base.ImageTabularChartReader",
                "ipynb": "openagent.knowledgebase.document_loaders.file.ipynb.base.IPYNBReader",
                "json": "openagent.knowledgebase.document_loaders.file.json.base.JSONReader",
                "markdown": "openagent.knowledgebase.document_loaders.file.markdown.base.MarkdownReader",
                "mbox": "openagent.knowledgebase.document_loaders.file.mbox.base.MboxReader",
                "paged_csv": "openagent.knowledgebase.document_loaders.file.paged_csv.base.PagedCSVReader",
                "pandas_csv": "openagent.knowledgebase.document_loaders.file.pandas_csv.base.PandasCSVReader",
                "pandas_excel": "openagent.knowledgebase.document_loaders.file.pandas_excel.base.PandasExcelReader",
                "pdf": "openagent.knowledgebase.document_loaders.file.pdf.base.PDFReader",
                "pdf_miner": "openagent.knowledgebase.document_loaders.file.pdf_miner.base.PDFMinerReader",
                "pptx": "openagent.knowledgebase.document_loaders.file.pptx.base.PptxReader",
                "pymu_pdf": "openagent.knowledgebase.document_loaders.file.pymu_pdf.base.PyMuPDFReader",
                "rdf": "openagent.knowledgebase.document_loaders.file.rdf.base.RDFReader",
                "simple_csv": "openagent.knowledgebase.document_loaders.file.simple_csv.base.SimpleCSVReader",
                "unstructured": "openagent.knowledgebase.document_loaders.file.unstructured.base.UnstructuredReader",
                "firebase_realtimedb": "openagent.knowledgebase.document_loaders.firebase_realtimedb.base.FirebaseRealtimeDatabaseReader",
                "firestore": "openagent.knowledgebase.document_loaders.firestore.base.FirestoreReader",
                "github_repo_issues": "openagent.knowledgebase.document_loaders.github_repo_issues.base.GitHubRepositoryIssuesReader",
                "gmail": "openagent.knowledgebase.document_loaders.gmail.base.GmailReader",
                "google_calendar": "openagent.knowledgebase.document_loaders.google_calendar.base.GoogleCalendarReader",
                "google_docs": "openagent.knowledgebase.document_loaders.google_docs.base.GoogleDocsReader",
                "google_keep": "openagent.knowledgebase.document_loaders.google_keep.base.GoogleKeepReader",
                "google_sheets": "openagent.knowledgebase.document_loaders.google_sheets.base.GoogleSheetsReader",
                "gpt_repo": "openagent.knowledgebase.document_loaders.gpt_repo.base.GPTRepoReader",
                "graphdb_cypher": "openagent.knowledgebase.document_loaders.graphdb_cypher.base.GraphDBCypherReader",
                "graphql": "openagent.knowledgebase.document_loaders.graphql.base.GraphQLReader",
                "hatena_blog": "openagent.knowledgebase.document_loaders.hatena_blog.base.HatenaBlogReader",
                "hubspot": "openagent.knowledgebase.document_loaders.hubspot.base.HubspotReader",
                "huggingface_fs": "openagent.knowledgebase.document_loaders.huggingface.fs.base.HuggingFaceFSReader",
                "intercom": "openagent.knowledgebase.document_loaders.intercom.base.IntercomReader",
                "jira": "openagent.knowledgebase.document_loaders.jira.base.JiraReader",
                # "joplin": "openagent.knowledgebase.document_loaders.joplin.base.JoplinReader",
                "jsondata": "openagent.knowledgebase.document_loaders.jsondata.base.JSONDataReader",
                "kaltura_esearch": "openagent.knowledgebase.document_loaders.kaltura.esearch.base.KalturaESearchReader",
                "kibela": "openagent.knowledgebase.document_loaders.kibela.base.KibelaReader",
                # "make_com": "openagent.knowledgebase.document_loaders.make_com.base.MakeWrapper",
                "mangoapps_guides": "openagent.knowledgebase.document_loaders.mangoapps_guides.base.MangoppsGuidesReader",
                "maps": "openagent.knowledgebase.document_loaders.maps.base.OpenMap",
                "memos": "openagent.knowledgebase.document_loaders.memos.base.MemosReader",
                "metal": "openagent.knowledgebase.document_loaders.metal.base.MetalReader",
                "milvus": "openagent.knowledgebase.document_loaders.milvus.base.MilvusReader",
                "mondaydotcom": "openagent.knowledgebase.document_loaders.mondaydotcom.base.MondayReader",
                "mongo": "openagent.knowledgebase.document_loaders.mongo.base.SimpleMongoReader",
                "notion": "openagent.knowledgebase.document_loaders.notion.base.NotionPageReader",
                "obsidian": "openagent.knowledgebase.document_loaders.obsidian.base.ObsidianReader",
                "opendal": "openagent.knowledgebase.document_loaders.opendal_reader.base.OpendalReader",
                "opendal_azblob": "openagent.knowledgebase.document_loaders.opendal_reader.azblob.base.OpendalAzblobReader",
                "opendal_gcs": "openagent.knowledgebase.document_loaders.opendal_reader.gcs.base.OpendalGcsReader",
                "opendal_s3": "openagent.knowledgebase.document_loaders.opendal_reader.s3.base.OpendalS3Reader",
                "outlook_localcalendar": "openagent.knowledgebase.document_loaders.outlook_localcalendar.base.OutlookLocalCalendarReader",
                "pubmed": "openagent.knowledgebase.document_loaders.papers.pubmed.base.PubmedReader",
                "pinecone": "openagent.knowledgebase.document_loaders.pinecone.base.PineconeReader",
                "qdrant": "openagent.knowledgebase.document_loaders.qdrant.base.QdrantReader",
                "readwise": "openagent.knowledgebase.document_loaders.readwise.base.ReadwiseReader",
                "reddit": "openagent.knowledgebase.document_loaders.reddit.base.RedditReader",
                "slack": "openagent.knowledgebase.document_loaders.slack.base.SlackReader",
                "snscrape_twitter": "openagent.knowledgebase.document_loaders.snscrape_twitter.base.SnscrapeTwitterReader",
                "spotify": "openagent.knowledgebase.document_loaders.spotify.base.SpotifyReader",
                "stackoverflow": "openagent.knowledgebase.document_loaders.stackoverflow.base.StackoverflowReader",
                "steamship": "openagent.knowledgebase.document_loaders.steamship.base.SteamshipFileReader",
                "string_iterable": "openagent.knowledgebase.document_loaders.string_iterable.base.StringIterableReader",
                "trello": "openagent.knowledgebase.document_loaders.trello.base.TrelloReader",
                "twitter": "openagent.knowledgebase.document_loaders.twitter.base.TwitterTweetReader",
                "weather": "openagent.knowledgebase.document_loaders.weather.base.WeatherReader",
                "weaviate": "openagent.knowledgebase.document_loaders.weaviate.base.WeaviateReader",
                "async_web": "openagent.knowledgebase.document_loaders.web.async_web.base.AsyncWebPageReader",
                "beautiful_soup_web": "openagent.knowledgebase.document_loaders.web.beautiful_soup_web.base.BeautifulSoupWebReader",
                "knowledge_base_web": "openagent.knowledgebase.document_loaders.web.knowledge_base.base.KnowledgeBaseWebReader",
                # "readability_web": "openagent.knowledgebase.document_loaders.web.readability_web.base.ReadabilityWebPageReader",
                "rss": "openagent.knowledgebase.document_loaders.web.rss.base.RssReader",
                "simple_web": "openagent.knowledgebase.document_loaders.web.simple_web.base.SimpleWebPageReader",
                # "sitemap": "openagent.knowledgebase.document_loaders.web.sitemap.base.SitemapReader",
                "trafilatura_web": "openagent.knowledgebase.document_loaders.web.trafilatura_web.base.TrafilaturaWebReader",
                "unstructured_web": "openagent.knowledgebase.document_loaders.web.unstructured_web.base.UnstructuredURLLoader",
                "whatsapp": "openagent.knowledgebase.document_loaders.whatsapp.base.WhatsappChatLoader",
                "wikipedia": "openagent.knowledgebase.document_loaders.wikipedia.base.WikipediaReader",
                "wordlift": "openagent.knowledgebase.document_loaders.wordlift.base.WordLiftLoader",
                "wordpress": "openagent.knowledgebase.document_loaders.wordpress.base.WordpressReader",
                "youtube_transcript": "openagent.knowledgebase.document_loaders.youtube_transcript.base.YoutubeTranscriptReader",
                "zendesk": "openagent.knowledgebase.document_loaders.zendesk.base.ZendeskReader",
                "zulip": "openagent.knowledgebase.document_loaders.zulip.base.ZulipReader",
}
    reader_class = import_class(mapping[reader_type])
    return reader_class