import random
import base64
import hashlib
import logging
from Crypto import Random
from Crypto.Cipher import AES

def generate_enp(hash_string):
	binary_value = bin(int(hash_string, 16))[2:].zfill(256)
	random.seed(50)
	indexes = [i for i in range(256)]
	random.shuffle(indexes)
	shuffled_hash = ''.join([binary_value[index] for index in indexes])
	negative_password_before_pi = []
	
	for count in range(1, 257):
		num = shuffled_hash[:count]
		# 1000 0
		num = num[:-1] + '0' if num[-1] == '1' else num[:-1] + '1'
		num += '*'*(256-count)
		print(num)
		negative_password_before_pi.append(num)

	negative_password_after_pi = []
	
	for count in range(0, 256):
		starred_string = '*'*256
		new_num = negative_password_before_pi[count]
		starred_list = list(starred_string)
		for index_counter in range(0, count+1):
			index = indexes[index_counter]
			starred_list[index] = new_num[index_counter]
			# print(starred_list)
		negative_password_after_pi.append(''.join(starred_list))

	encoded_passwords = []
	# iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])
	iv = Random.new().read(AES.block_size)
	# key = bin(int(hash_string, 16))[2:]
	key = hash_string[:32] #'2abaec27cb5baab6bb7cad1f58e6e0be'
	aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
	for password in negative_password_after_pi:
		encoded_password = password
		encoded_password = encoded_password.replace("0", "00")
		encoded_password = encoded_password.replace("1", "01")
		while encoded_password.find('*') != -1:
			encoded_password = encoded_password.replace("*", random.choice(["10","11"]),1)
		data = hex(int(encoded_password, 2))[2:].zfill(128)
		# encoded_passwords.append(str(base64.b64encode(aes.encrypt(data)),'utf-8'))
		encoded_passwords.append((aes.encrypt(data).hex()))
	ENP = ' || '.join(encoded_passwords)
	# b64_string = str(base64.b64encode(aes.encrypt(data)),'utf-8')
	return ENP