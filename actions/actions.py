from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionConsultarSaldo(Action):

    def name(self) -> Text:
        return "action_consultar_saldo"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        saldo = 850.00

        dispatcher.utter_message(
            text=f"Seu saldo simulado é de R$ {saldo:.2f}."
        )

        return []


class ActionRealizarPix(Action):

    def name(self) -> Text:
        return "action_realizar_pix"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        valor_pix = tracker.get_slot("valor_pix")
        destinatario_pix = tracker.get_slot("destinatario_pix")

        dispatcher.utter_message(
            text=f"Pix simulado realizado com sucesso! Foram enviados R$ {valor_pix} para {destinatario_pix}."
        )

        return [
            SlotSet("valor_pix", None),
            SlotSet("destinatario_pix", None)
        ]