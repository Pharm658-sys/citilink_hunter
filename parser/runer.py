from playwright.async_api import async_playwright

async def main(page_number: int = 1, max_items: int = 10):
	laptops = []
	count = 0


	async with async_playwright() as p:
		browser = await p.chromium.launch(headless=False)
		context = await browser.new_context()
		page = await context.new_page()

# вход парсера на сайт
		await page.goto(f"https://www.citilink.ru/catalog/noutbuki/?ref=mainmenu_plate&p={page_number}",wait_until="domcontentloaded", timeout=30000)
		await page.wait_for_timeout(5000)



		await page.wait_for_selector("a[data-meta-name='Snippet__title']")

		titles = await page.locator("a[data-meta-name='Snippet__title']").all_text_contents()

		links = await page.locator("a[data-meta-name='Snippet__title']").evaluate_all(
			"(elements) => elements.map(el => el.href)"
		)

		prices = await page.locator("span[class*='MainPriceNumber']").all_text_contents()

# выведение данных в чат бота
		for title, price, link in zip(titles, prices, links):
			laptops.append({
				"title": title,
				"price": price,
				"link": link
			})
			print(f"{title}\nЦена: {price}\nСсылка: {link}\n{'-'*50}")

			count += 1
			if count >= max_items:
				break

		await browser.close()
		return laptops
















