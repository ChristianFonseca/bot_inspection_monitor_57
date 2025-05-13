from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import os
import boto3
from dotenv import load_dotenv

load_dotenv()

url = 'https://www.samsung.com/pe/monitors/all-monitors/?57-inch'

def notify_via_sns(subject: str, message: str) -> None:
    sns = boto3.client("sns", 
                       aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
                       aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
                       region_name=os.environ.get("AWS_REGION", "us-east-1"))
    topic_arn = os.environ["SNS_TOPIC_ARN"]

    sns.publish(
        TopicArn=topic_arn,
        Subject=subject,
        Message=message
    )

def main():
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Ejecutar en modo headless
    options.add_argument('--disable-gpu')  # Deshabilitar GPU para mejor rendimiento
    options.add_argument('--no-sandbox')  # Deshabilitar sandbox para mejor rendimiento
    options.add_argument('--disable-dev-shm-usage')  # Evitar problemas de memoria
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    contenedores = soup.find_all('div', class_='pd19-product-card__cta-wrap')
    nombres = []
    for contenedor in contenedores:
        nombre_contain = contenedor.find('button', class_='cta cta--contained cta--black pd19-product-card__cta--buy-now js-pfv2-buy-now')
        if nombre_contain:
            nombre = nombre_contain.text.strip()
            nombres.append(nombre)

    message = f"""
    Hay productos:
    URL: {url}
    """

    if len(nombres) > 0:
        notify_via_sns('Samsung Monitors', message)

if __name__ == '__main__':
    main()
