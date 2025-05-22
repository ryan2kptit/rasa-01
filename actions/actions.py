from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import json

class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        crypto_type = tracker.get_slot("crypto_type")
        
        # Mock balance data - trong thực tế sẽ kết nối với API ví
        balances = {
            "BTC": 0.5,
            "ETH": 2.3,
            "BNB": 150.0,
            "USDT": 1000.0,
            "EOS": 500.0
        }
        
        if crypto_type:
            balance = balances.get(crypto_type.upper(), 0)
            message = f"Số dư {crypto_type.upper()} của bạn: {balance}"
        else:
            message = "Tổng số dư ví của bạn:\n"
            for crypto, amount in balances.items():
                if amount > 0:
                    message += f"• {crypto}: {amount}\n"
        
        dispatcher.utter_message(text=message)
        return []

class ActionGetCryptoPrice(Action):
    def name(self) -> Text:
        return "action_get_crypto_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        crypto_type = tracker.get_slot("crypto_type")
        
        if not crypto_type:
            dispatcher.utter_message(template="utter_ask_crypto_type")
            return []
        
        # Mock price data - trong thực tế sẽ gọi API như CoinGecko
        prices = {
            "BTC": 45000.0,
            "ETH": 3200.0,
            "BNB": 420.0,
            "USDT": 1.0,
            "EOS": 1.25,
            "ADA": 0.45,
            "SOL": 98.0,
            "LINK": 15.5,
            "DOT": 7.2,
            "LTC": 180.0
        }
        
        price = prices.get(crypto_type.upper(), 0)
        
        if price > 0:
            message = f"💰 Giá hiện tại của {crypto_type.upper()}: ${price:,.2f} USDT"
            dispatcher.utter_message(text=message)
            return [SlotSet("price", price)]
        else:
            dispatcher.utter_message(text=f"Không tìm thấy giá cho {crypto_type}")
            return []

class ActionExecuteTransfer(Action):
    def name(self) -> Text:
        return "action_execute_transfer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        amount = tracker.get_slot("amount")
        crypto_type = tracker.get_slot("crypto_type")
        contact_name = tracker.get_slot("contact_name")
        
        # Thực hiện giao dịch chuyển tiền (mock)
        # Trong thực tế sẽ kết nối với blockchain networks
        
        transaction_id = "tx_" + str(hash(f"{amount}{crypto_type}{contact_name}"))[-8:]
        
        message = f"🎉 Chuyển tiền thành công!\n"
        message += f"• Số lượng: {amount} {crypto_type.upper()}\n"
        message += f"• Người nhận: {contact_name}\n"
        message += f"• Transaction ID: {transaction_id}\n"
        message += f"• Phí giao dịch: $0.15"
        
        dispatcher.utter_message(text=message)
        
        # Clear slots sau khi hoàn thành giao dịch
        return [
            SlotSet("amount", None),
            SlotSet("crypto_type", None),
            SlotSet("contact_name", None)
        ]

class ActionExecuteBuy(Action):
    def name(self) -> Text:
        return "action_execute_buy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        amount = tracker.get_slot("amount")
        crypto_type = tracker.get_slot("crypto_type")
        price = tracker.get_slot("price")
        
        # Thực hiện giao dịch mua (mock)
        if price:
            total_cost = float(amount) * float(price)
            message = f"✅ Mua thành công {amount} {crypto_type.upper()}\n"
            message += f"• Giá: ${price} USDT\n"
            message += f"• Tổng tiền: ${total_cost:,.2f} USDT"
        else:
            message = f"✅ Mua thành công {amount} {crypto_type.upper()} với giá thị trường"
        
        dispatcher.utter_message(text=message)
        
        return [
            SlotSet("amount", None),
            SlotSet("crypto_type", None),
            SlotSet("price", None)
        ]

class ActionExecuteSell(Action):
    def name(self) -> Text:
        return "action_execute_sell"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        amount = tracker.get_slot("amount")
        crypto_type = tracker.get_slot("crypto_type")
        price = tracker.get_slot("price")
        
        # Thực hiện giao dịch bán (mock)
        if price:
            total_revenue = float(amount) * float(price)
            message = f"✅ Bán thành công {amount} {crypto_type.upper()}\n"
            message += f"• Giá: ${price} USDT\n"
            message += f"• Tổng thu: ${total_revenue:,.2f} USDT"
        else:
            message = f"✅ Bán thành công {amount} {crypto_type.upper()} với giá thị trường"
        
        dispatcher.utter_message(text=message)
        
        return [
            SlotSet("amount", None),
            SlotSet("crypto_type", None),
            SlotSet("price", None)
        ]

class ActionSearchContact(Action):
    def name(self) -> Text:
        return "action_search_contact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        contact_name = tracker.get_slot("contact_name")
        
        # Mock contact database
        contacts = {
            "john": "0x742d35Cc6634C0532925a3b8D404Fd67C5e096bBa",
            "alice": "0x8ba1f109551bD432803012645Hac136c9db5b81b",
            "bob": "0x42d35Cc6634C0532925a3b8D404Fd789e096cCa",
            "mẹ": "0x9d8A8f4b123456789abcdef0123456789abcdef0",
            "anh tuấn": "0xdef0123456789abcdef0123456789abcdef012345",
            "bạn thân": "0x456789abcdef0123456789abcdef0123456789ab"
        }
        
        if contact_name:
            contact_key = contact_name.lower()
            wallet_address = contacts.get(contact_key)
            
            if wallet_address:
                message = f"✅ Tìm thấy liên hệ '{contact_name}'\n"
                message += f"Địa chỉ ví: {wallet_address[:10]}...{wallet_address[-6:]}"
                return [SlotSet("wallet_address", wallet_address)]
            else:
                message = f"❌ Không tìm thấy liên hệ '{contact_name}' trong danh bạ"
                dispatcher.utter_message(text=message)
                return []
        
        # Hiển thị danh sách liên hệ
        message = "📞 Danh bạ của bạn:\n"
        for name, address in contacts.items():
            message += f"• {name}: {address[:10]}...{address[-6:]}\n"
        
        dispatcher.utter_message(text=message)
        return []

class ActionRequireBiometric(Action):
    def name(self) -> Text:
        return "action_require_biometric"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Mock biometric authentication
        message = "🔐 Vui lòng xác thực bằng vân tay hoặc Face ID để tiếp tục giao dịch."
        dispatcher.utter_message(text=message)
        
        # Simulate successful biometric auth
        # Trong thực tế sẽ tích hợp với biometric SDK
        success_message = "✅ Xác thực thành công! Tiếp tục giao dịch..."
        dispatcher.utter_message(text=success_message)
        
        return []

class ActionCheckNetworkFee(Action):
    def name(self) -> Text:
        return "action_check_network_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        crypto_type = tracker.get_slot("crypto_type")
        network_type = tracker.get_slot("network_type")
        
        # Mock network fees
        fees = {
            "BTC": "$2.50 - $5.00",
            "ETH": "$15.00 - $30.00",
            "BNB": "$0.10 - $0.50",
            "EOS": "$0.01 - $0.05",
            "USDT": "$15.00 - $30.00 (ERC-20)"
        }
        
        if crypto_type:
            fee = fees.get(crypto_type.upper(), "$0.10 - $2.00")
            message = f"💰 Phí chuyển {crypto_type.upper()}: {fee}"
        else:
            message = "💰 Phí giao dịch theo mạng:\n"
            for crypto, fee in fees.items():
                message += f"• {crypto}: {fee}\n"
        
        dispatcher.utter_message(text=message)
        return []

class ActionValidateWalletAddress(Action):
    def name(self) -> Text:
        return "action_validate_wallet_address"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        wallet_address = tracker.get_slot("wallet_address")
        
        if not wallet_address:
            dispatcher.utter_message(text="Vui lòng cung cấp địa chỉ ví hợp lệ")
            return []
        
        # Basic validation (trong thực tế cần validation phức tạp hơn)
        if len(wallet_address) >= 26 and wallet_address.startswith('0x'):
            message = f"✅ Địa chỉ ví hợp lệ: {wallet_address[:10]}...{wallet_address[-6:]}"
            dispatcher.utter_message(text=message)
            return []
        else:
            message = "❌ Địa chỉ ví không hợp lệ. Vui lòng kiểm tra lại."
            dispatcher.utter_message(text=message)
            return [SlotSet("wallet_address", None)]