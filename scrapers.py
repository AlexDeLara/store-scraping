import requests
import json

class ScraperTypeA():
	def __init__(self, base_url, headers):
		self.base_url = base_url
		self.headers = headers

		def __get_response_data(parsed, keys):
			if len(keys) == 1:
				return parsed.get(keys[0], [])
			
			return __get_response_data(parsed, keys[1:])


		def run():
			url = base_url.format(params)

			response = requests.request("GET", url, headers=headers)

			if response.ok is False:
				# Retry logic
				pass
			
			parsed = json.loads(response.text)


		


					 



# Algorithm
# 1. Format URL query
# 2. Update header
# 3. Send request
# 4. Check response
# 5. if success, parse response. Else, retry logic
# 6. dump data


base_url = "https://www.liverpool.com.mx/getPlpFilter?{query_params}"

query_params = {
		'categoryId': '',
		'page': '',
		'Path': '',
		'encryptedURL': ''
}

headers = {   
		'authority': 'www.liverpool.com.mx',
		'accept': 'application/json, text/plain, */*',
		'accept-language': 'en-US,en;q=0.9',
		'authorization': '[object Object]',
		'brand': 'LP',
		'channel': 'WEB',
		'cookie': '_gcl_au=1.1.2095957366.1666661995; _evga_fb08={%22uuid%22:%22a34abf66b24543f7%22}; _tt_enable_cookie=1; _ttp=2b97535e-03af-44e3-9be4-e14514c15e1b; _pin_unauth=dWlkPU9USTVaVEZsTldFdE5qbGxOeTAwTXpGaExXRTNZVFF0WkdRNU4yVXdOMkkwT0RJMQ; mdLogger=false; kampyle_userid=e6e8-b12c-c25e-a360-ea55-a508-ce37-bdf0; genero=x; segment=fuero; _sfid_a127={%22anonymousId%22:%22a34abf66b24543f7%22%2C%22consents%22:[]}; _scid=3fb8622f-2ff4-459a-ae3a-cff7caf2db33; _sctr=1|1666587600000; _fbp=fb.2.1666661998792.1842020424; gbi_visitorId=cl9njiui700012v73pqg99ctx; FPID=FPID2.3.EGMAGAqlZuw8guCdl2%2FXJt99QImnRoYH0IdcpPMirX8%3D.1666661996; fita.sid.liverpool=H3eEeq3oEsUsdETWud57CirPBDltlQEB; DCC=SiteD; sfEngine=elastic; akacd_RWASP-default-phased-release=3844624225~rv=31~id=8b01439541d1a9b50798fe133696db16; PIM-SESSION-ID=rrwJeou73ACDaanH; rxVisitor=1667171425587NKT815SPQFPEUMJV38ED3AN8PRV1FRFS; dtCookie=v_4_srv_5_sn_B55GR907CGJI019TDUSM7JTUKBEHB2S4_perc_100000_ol_0_mul_1_app-3Afb4b113cea6706c5_0_rcs-3Acss_0; _gid=GA1.3.327179040.1667171428; TT3bl=false; TURNTO_VISITOR_SESSION=1; calNeOpcS=true; enblNeEdCaFCrt=true; enblNeEdCaFPdp=true; _abck=75914C7DD8D4A23BC23471208417FF3D~0~YAAQcdeQyUic3TOEAQAAC8CiNAj6SGTtShdzJwbL3duLUQbH9wHd70LdkcaHL/t7wWv9rrs2elmD7qhFyxkUi77jNV5dYhmsExHdufAoUlVSJI34udHVMDQJePBUtP0u2KobX+jXsc2/onJHg18kyIDzxPZxb9euW21VgWoQl9/mKCIZrHUrZ5AHD92Ub7rPRZOY/SaMTAe9UFaMp0XzFfNkv5JMXHutdpcosgPQV33DDEV0OH4NHij1iI+ky43l/xyd9Y9DwcTBcEgUsLEmn2JEL21fDfSnNnatyzjDiKWJx/qDuYANPOoti7+qZg9CzrdA+p5xYhFE6HPgKFX6SLd5D2krqhFZu8adL3RmHQ/4oheJdQrPCalkdyTWKnFSzwcdsc78g/a1xkTksg751gANXiMh/nnsAgFXqzU=~-1~-1~-1; bm_sz=EF9A3C038C6B6729105C25B752108188~YAAQcdeQyUqc3TOEAQAAC8CiNBFHf1lFob3ysPOhwwqcE8gw3BdzC419ggLqwfi0VJQNHuY6P5zxJu1nTiRUSzWivZkuBjNZK30ONDC8z6faN8VR1jE8cGwEuWPw5G0+WqogB1WVZt32ItQhxTnm+JF2jlfMxmbhg7xKbS3KwpqrdQhuWVIY/U3V2i3BDECUd+IhBMJPE1/ruaBNC6PoFiDn8Rxeuv1JboB2XLZKAlOGZ5PWggQ+fVQpbgYf/Lq+EBJvuWoRKNOMkxzYR8ZKkhP9We0OiE0Lyj2O/X1daEsIIzw1256TDJw=~4338225~4535605; TURNTO_TEASER_SHOWN=1667333419651; _gac_=1.1667333967.CjwKCAjwh4ObBhAzEiwAHzZYUwgYwv1ELLfnkxUIDAOF3biwzNibVPe_-_HfGOqCLQkjC82Nzy_0_xoCAzIQAvD_BwE; _gac_UA-4668284-1=1.1667333967.CjwKCAjwh4ObBhAzEiwAHzZYUwgYwv1ELLfnkxUIDAOF3biwzNibVPe_-_HfGOqCLQkjC82Nzy_0_xoCAzIQAvD_BwE; _gac_UA-4668284-55=1.1667333967.CjwKCAjwh4ObBhAzEiwAHzZYUwgYwv1ELLfnkxUIDAOF3biwzNibVPe_-_HfGOqCLQkjC82Nzy_0_xoCAzIQAvD_BwE; _gcl_aw=GCL.1667333967.CjwKCAjwh4ObBhAzEiwAHzZYUwgYwv1ELLfnkxUIDAOF3biwzNibVPe_-_HfGOqCLQkjC82Nzy_0_xoCAzIQAvD_BwE; _gcl_dc=GCL.1667333967.CjwKCAjwh4ObBhAzEiwAHzZYUwgYwv1ELLfnkxUIDAOF3biwzNibVPe_-_HfGOqCLQkjC82Nzy_0_xoCAzIQAvD_BwE; dtSa=-; JSESSIONID=aYI0_E5XTyo5ykvLxhoOocSH33NhOAtCOBWeCEpqdtMsvtHwRsCx!615469158; mf_4b65f806-7a98-46e9-bed7-78c70a09f4dd=|.-5276703658.1667336266218|1667171426795||0|||0|0|5.07882; RT="z=1&dm=www.liverpool.com.mx&si=4727c86b-62df-4b98-9e55-bb37bea01f53&ss=l9yngr1g&sl=6&tt=7wo&obo=3&rl=1"; cto_bundle=9tMKc19zczVtU0lyM3pOZjJEalVhNXdUJTJGN2QlMkJhR3hVejhIRE1oVUdRazlnUTN2dnROdTFRQjZTJTJGNlRKczFMZmhJekdoZUk3NVFaekRCVmdMRlQzc2VzM2FTeFF0Znp1dTF1WHhIRE9iVEIxYktka2hrbTVuNmoyQ2paVzIlMkZ2VFY2QWpkendHZ3N2OW9aOGtuRmZsWXVRJTJCSTd4JTJGbjNrRWJJVUR2Wk4lMkZjZFdSREdYTSUzRA; _derived_epik=dj0yJnU9NlFyaTVEVi1BeXNwOWlRZjQ0TWxaa2pGa0Naei15LTAmbj1xNk5DcHZYR1FibTVsVlBlcTFnbDRRJm09MSZ0PUFBQUFBR05oaUVzJnJtPTEmcnQ9QUFBQUFHTmhpRXMmc3A9Mg; _ga=GA1.1.1792263991.1666661996; kampyleUserSession=1667336268539; kampyleUserSessionsCount=10; kampyleSessionPageCounter=1; akavpau_allow=1667336330~id=8387be15605821a49f058ef21d4d52b7; dtLatC=1; _ga_0WY68EFMNB=GS1.1.1667336260.8.0.1667336273.0.0.0; _ga_171XPPQ282=GS1.1.1667336260.8.1.1667336273.47.0.0; _dc_gtm_UA-4668284-1=1; _ga_ZF6SNY8CLK=GS1.1.1667343429.9.0.1667343431.58.0.0; rxvt=1667211796707|1667336121454; dtPC=5$409004027_22h20vGFPMFNTLGBDTFFMTWUFCEHHFERAPINBP-0e0; _abck=75914C7DD8D4A23BC23471208417FF3D~-1~YAAQB9eQyXad9B2EAQAAKrbxNAijHMqeda856r3m9BIo82hRjSZBmCdst2SNsSnmO6wn0KDqDh0sRWjzLfZdmAKZsjR0bH2y+Efk5EgB8bHPJCQFJAY8tKn9uVTXTsIYfCatD4sJWRd75/suw3X6XG5yk7FKEkb7O55u9ARw5Yl37duALVrky2+Jqs8yHTWEt1NnRI5JQkcgiffG2tOAw8xRuxqDV7LoKcjcEI9gB5rKYEvwqHnQeF73me5RhViEr4Sj2nIiOamoOYC/69ja+DUmq8HGYTCnnYZdnRB0y4skQWMTVShPAT/p/U/j4oSayHM7Oufdo3pWx2q1ikW2pWlvmzovEhWjG4hQNlc7eTYNqG3t0EvWx224mM+NpC26jbtCYAcSlw8eyHoI7ckMigeYm5EqSb49pek/8R4=~0~-1~-1; akavpau_allow=1667335626~id=764809361acf2e618fb8dc8a6d3d17c6',
		'customerid': '',
		'referer': 'https://www.liverpool.com.mx',
		'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Linux"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'static-cache': 'true',
		'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
		'user-correlation-id': 'LP-WEB-4707bcc3-f101-46af-b061-abb0eeb3268c',
		'x-correlation-id': 'LP-WEB-4707bcc3-f101-46af-b061-abb0eeb3268c',
		'x-dtpc': '5$409004027_22h20vGFPMFNTLGBDTFFMTWUFCEHHFERAPINBP-0e0'
}

params = base_params.format(**payload)

				url = self.format_url(base_url=base_url, params=params, store=store)

response = requests.request("GET", url, headers=headers)

if(response.ok):
					parsed = json.loads(response.text)
					