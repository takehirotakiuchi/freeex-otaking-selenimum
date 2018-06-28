from freeex_libs import freeex_selenium, json_manager
import settings

def main():
	selenium = freeex_selenium.FreeexSelenium()
	selenium.login()

	manager = json_manager.JsonManager()
	records = manager.load()
	for record in records:
		if not record['is-saved']:
			selenium.regist_newsletter(record)
			manager.store(record)

	selenium.quite()

if __name__ == '__main__':
	main()