from selenium.webdriver.common.by import By

ORDER_ITEM = By.CLASS_NAME, 'OrderHistory_listItem__2x95r'
ORDER_ITEM_LIST = By.CLASS_NAME, 'OrderFeed_list__OLh59'
ORDER_DETAILS_POPUP = By.CLASS_NAME, 'Modal_orderBox__1xWdi'
ORDER_COUNTER_ALL_TIME = By.CSS_SELECTOR, '.OrderFeed_ordersData__1L6Iv div:nth-child(2) p.OrderFeed_number__2MbrQ'
ORDER_COUNTER_TODAY = By.CSS_SELECTOR, '.OrderFeed_ordersData__1L6Iv div:nth-child(3) p.OrderFeed_number__2MbrQ'
ORDER_IN_PROGRESS = By.CLASS_NAME, 'OrderFeed_orderListReady__1YFem'
