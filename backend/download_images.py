from icrawler.builtin import BingImageCrawler
import os

categories = [
    'normal', 'oily', 'dry', 'combination', 'sensitive',
    'acne_prone', 'dehydrated', 'mature_skin', 'hyperpigmented_skin',
    'redness_rosacea', 'textured', 'dull_skin', 'eczema',
    'allergy_prone', 'sun_damaged', 'uneven_tone', 'pimple_prone',
    'open_pores', 'healthy_skin'
]  # Shortened for test
base_dir = 'dataset'

for category in categories:
    folder_name = category.replace(" ", "_").lower()
    save_dir = os.path.join(base_dir, folder_name)
    os.makedirs(save_dir, exist_ok=True)
    
    print(f"Downloading '{category}' images to {save_dir}...")
    crawler = BingImageCrawler(storage={'root_dir': save_dir})
    crawler.crawl(keyword=category, max_num=200)  # Start small to test
