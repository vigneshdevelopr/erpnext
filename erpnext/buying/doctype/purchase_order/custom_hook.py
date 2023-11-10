# # import frappe
# # import requests
# # import json

# # def send_purchase_order_for_signature(purchase_order):
# #     # Get the DocuSign API key and secret key
# #     docusign_api_key = frappe.db.get_value("Global Defaults", None, "docusign_api_key")
# #     docusign_secret_key = frappe.db.get_value("Global Defaults", None, "docusign_secret_key")

# #     # Generate a DocuSign envelope for the purchase order
# #     envelope = {
# #         "documents": [
# #             {
# #                 "name": purchase_order.name,
# #                 "content": purchase_order.pdf_file_data
# #             }
# #         ],
# #         "signers": [
# #             {
# #                 "email": purchase_order.supplier.email,
# #                 "name": purchase_order.supplier.name,
# #                 "roleName": "Supplier"
# #             }
# #         ]
# #     }

# #     # Send the DocuSign envelope
# #     headers = {
# #         "Authorization": f"Bearer {docusign_api_key}"
# #     }

# #     response = requests.post(
# #         "https://demo.docusign.net/restapi/v2/accounts/1234567890/envelopes",
# #         headers=headers,
# #         json=envelope
# #     )

# #     if response.status_code != 201:
# #         raise Exception("Failed to send DocuSign envelope")

# #     # Update the purchase order status to "Sent for signature"
# #     frappe.db.set_value("Purchase Order", purchase_order.name, "status", "Sent for signature")

# # # Add a custom button to the purchase order print page
# # frappe.ui.form.on("Purchase Order", "print", send_purchase_order_for_signature)



# # ==========================================


# import frappe
# import requests
# import json

# def send_purchase_order_for_signature(purchase_order):
#     try:
#         # Get the DocuSign API key and secret key
#         docusign_api_key = frappe.db.get_value("Global Defaults", None, "docusign_api_key")
#         docusign_secret_key = frappe.db.get_value("Global Defaults", None, "docusign_secret_key")

#         if not docusign_api_key or not docusign_secret_key:
#             frappe.msgprint("DocuSign API credentials are missing. Please configure them.")
#             return

#         # Generate a DocuSign envelope for the purchase order
#         envelope = {
#             "documents": [
#                 {
#                     "name": purchase_order.name,
#                     "content": purchase_order.pdf_file_data
#                 }
#             ],
#             "signers": [
#                 {
#                     "email": purchase_order.supplier.email,
#                     "name": purchase_order.supplier.name,
#                     "roleName": "Supplier"
#                 }
#             ]
#         }

#         # Send the DocuSign envelope
#         headers = {
#             "Authorization": f"Bearer {docusign_api_key}"
#         }

#         response = requests.post(
#             "https://demo.docusign.net/restapi/v2/accounts/1234567890/envelopes",
#             headers=headers,
#             json=envelope
#         )

#         if response.status_code == 201:
#             # Update the purchase order status to "Sent for signature"
#             frappe.db.set_value("Purchase Order", purchase_order.name, "status", "Sent for signature")
#             frappe.msgprint(f"Purchase Order {purchase_order.name} sent for signature.")
#         else:
#             frappe.msgprint(f"Failed to send DocuSign envelope. Error: {response.status_code}")
#     except Exception as e:
#         frappe.msgprint(f"Error: {str(e)}")

# # Add a custom button to the purchase order print page
# frappe.ui.form.on("Purchase Order", "print", send_purchase_order_for_signature)

