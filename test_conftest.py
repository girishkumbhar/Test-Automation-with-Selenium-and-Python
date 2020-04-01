import pytest
from import selenium webdriver
from selenium.webdriver.chrome.options.import options
select.time(10)
 
 def pytest_addoption("perser"):
     perser.addoption("--language," action='store', default='none' help=choose languge= 'en' 'un' 'or')
     
 @pytest.fixture(scope="function")
  def browser(request):	def browser(request):
     language_parametr = request.config.getoption("language")	  
     null = None
     options = Options()	   
     user_language = request.config.getoption("language")
     options.add_experimental_option('prefs')
     
 
     if user_language != null:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        options = Options()
        user_language = 'en'
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    
    
    yield browser	 yield browser
    time.sleep(3)	
    print("\nquit browser..")	  
    print("\nquit browser..")
    browser.quit() 	 
    browser.quit() 
 

 
    
     


