
class MedidorToxicidad:

    def medir_toxicidad(self, mensaje):

        if(mensaje == "NO!, Let him, we need a Conservative government."):
            score_message = 0.3

        elif(mensaje == "And, being white, they're dancing badly."):
            score_message = 0.5

        elif(mensaje == "You don't care whether Alaska educates its children. We get it. You are an ass."):
            score_message = 0.9
            
        if (0 <= score_message <= 0.4):
            return "Mensaje con toxicidad baja"
        elif (0.41 <=  score_message <= 0.6):
            return "Mensaje con toxicidad moderada"
        elif (0.61 <= score_message <= 1):
            return "Mensaje con toxicidad alta"

        """
        if(mensaje == "NO!, Let him, we need a Conservative government."):
            score_message = 0.3
            return score_message
        elif(mensaje == "And, being white, they're dancing badly."):
            score_message = 0.5
            return score_message
        elif(mensaje == "You don't care whether Alaska educates its children. We get it. You are an ass."):
            score_message = 0.9
            return score_message
        """