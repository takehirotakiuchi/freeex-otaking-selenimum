# -*- coding: utf-8 -*-
import json
import glob
import os
import copy

class JsonManager():

	def __init__(self):
		self.data_dir = os.getenv("JSON_DIRECTORY")
		self.enable_memorize = self.str2bool(os.getenv("ENABLE_MEMORIZING", False))

	def str2bool(self, v):
		return v.lower() in ("yes", "true", "t", "1")

	def load(self):

		files = glob.glob('json/*')

		jsons = []
		for file in files:
			key = os.path.basename(file)
			with open(file, mode='r', encoding='utf-8') as f:
			  record = json.load(f)
			  record['path'] = file
			  jsons.append(record)

		return jsons

	def store(self, rawRecord):
		if not self.enable_memorize:
			return

		record = copy.deepcopy(rawRecord)
		path = record['path']
		del record['path']

		record['is-saved'] = True
		with open(path, mode='w', encoding='utf-8') as f:
			json.dump(record, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


	def store_body(self, rawRecord):
		with open(path, mode='w', encoding='utf-8') as f:
			json.dump(record, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
