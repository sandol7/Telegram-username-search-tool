import requests, random, os
import webbrowser
import time
webbrowser.open('https://t.me/Hardson404')
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
P = '\033[2;36m'
li = 'qwerty_uiop123_asdfghjkl456zxcvbnm7890'
li2 = 'qwerty_uiop123_asdfghjkl456zxcv.bnm.7890'

tok = input(X+'Token / ')
id = input('ID  / ')
print(Z)
os.system('clear')
def ch(user):
	url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
	headers = {
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-GB,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-US;q=0.6',
	'content-length': '60',
	'content-type': 'application/x-www-form-urlencoded',
	'cookie': 'mid=ZLKEwAABAAHtdtHRdaX_lsymh-LP; ig_did=91195A1C-EDD3-41A4-A025-8DE06DA3B630; ig_nrcb=1; dpr=2; datr=u4SyZE7bkZk5izvhol_OBLPF; shbid="6138\0542167209024\0541720959234:01f7004fbe7339dc33064143f2a4336cf4624560f0ef1703db1c642415bb9c36d0aa5200"; shbts="1689423234\0542167209024\0541720959234:01f7292500fd2ba50308e0660de4955b5c35f736b94b4b6117604472a8407e04496008a8"; csrftoken=euNcbMcFkmvymh9Lz7MoxbSOcXpst8TB',
	'origin': 'https://www.instagram.com',
	'referer': 'https://www.instagram.com/accounts/emailsignup/',
	'sec-ch-prefers-color-scheme': 'light',
	'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
	'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Linux"',
	'sec-ch-ua-platform-version': '""',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
	'viewport-width': '980',
	'x-asbd-id': '129477',
	'x-csrftoken': 'euNcbMcFkmvymh9Lz7MoxbSOcXpst8TB',
	'x-ig-app-id': '936619743392459',
	'x-ig-www-claim': '0',
	'x-instagram-ajax': '1007848011',
	'x-requested-with': 'XMLHttpRequest',
	}
	data = {
	'username': f'{user}',
	'opt_into_one_tap': 'false',
	}
	res = requests.post(url, headers=headers, data=data).text
	if "username_is_taken" in res:
		print(f'Bad Username : {user}')
	elif "username_only_has_number" in res:
		print(f'Bad Username : {user}')
	else:
		print(f'Good Username : {user}')
		requests.get("https://api.telegram.org/bot"+str(tok)+"/sendMessage?chat_id="+str(id)+"&text="+str(user))
def userra():
	while True:
		user1 = str("".join(random.choice(li)for i in range(1)))
		user2 = str("".join(random.choice(li2)for i in range(2)))
		user3 = str("".join(random.choice(li)for i in range(1)))
		user = user1+user2+user3
		ch(user)
def userra2():
	while True:
		user1 = str("".join(random.choice(li)for i in range(1)))
		user2 = str("".join(random.choice(li2)for i in range(2)))
		user3 = str("".join(random.choice(li)for i in range(1)))
		user4 = str("".join(random.choice(li3)for i in range(1)))
		aa = user2+user3+user4
		user5 = "".join(random.sample(aa, 4))
		user = user1+user5
		ch(user)

ascii_art = """

                 .  8@:Xt8S%tttt%8: X %8  .             
                .8.8:8;. .:: .. .    X8:X:8             
              ..X:8.  .  SXS8 .        .;8:@:           
             :@;X..     .:; t           .t.tSSS.        
            8S;%..       :. 8..           ..t:t8:.      
           :%8:.    %....:. 8;.....%        ::8t;       
        . 8:8;     .;;t..8. ;;8S;8t.         .:8.8.     
         %%:        ::;t::S X;%t;..           :.:X;.    
       . .t:         . ..:8t@..... .          ...%;;    
        ; @              .S @:t:8:.8            .8 t    
      . 8 X             ..; :SS:.%t;S8..         t.8;.  
      .::t:              :. 8S%%t::@ %%.        ..tt .  
      . 8%:             .:. X:.....tt 8..         t8..  
        8 %.             :: 8:..   %::8:.        ::8..  
       :% 8.            .:. @..  . ; St:       . 8:t.   
       ..:S;             :;tX..   ;;:S;        ..;S:    
       .:8.8:.           :88:   . : %.          @ @     
         .:%S:           ...     @ tt         .%tX      
           ;%.                 ..: @:         .%%%      
          .S;S8:               . 8 t%.      .;%%@:      
           :%:@:; .             ..8@%;8;   ..S8:.       
              :% @...             .;;.: . SSSt:         
              :t8@;.:              ....;8.@8:.          
              . ..X:.S:X8X;.     .%88 %;;S..            
                 ...;t8 . :%%:t%%  t @.:..              
                    ..:..t88@88888%% 

"""
for line in ascii_art.split('\n'):
    print(line)
    time.sleep(0.3)

P = '\033[2;36m'
F = '\033[2;32m'
Z = '\033[1;31m'

print(f'{P}1_ Four letters')
print('2_ quasi-quadrant\n')

print('TikTok:-  hardson404')
print('telegram:- @USV_W\n')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

try:
    num = int(input(f'{F}Choose the type of user :- '))
    if num == 1:
        import os
        os.system('clear')
        userra()
    elif num == 2:
        import os
        os.system('clear')
        userra2()
    else:
        print(Z + 'Please choose 1 or 2')
except:
    print(Z + '❌ Error: Please enter a valid number.')
