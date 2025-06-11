import itertools
import re

#Programa completamente generado por IA
frases = [
    "Aposté al EQUIPO.",
    "Aposté a CUOTA_NUMBER.",
    "Confié en JUGADOR.",
    "Jugué en CASA_APUESTAS.",
    "Compré CRYPTO.",
    "Me la jugué al EQUIPO.",
    "Aposté a la victoria de EQUIPO.",
    "Vi una CUOTA_NUMBER buena.",
    "Invertí todo en CRYPTO.",
    "Aposté que marcaba JUGADOR.",
    "CUOTA_CANTIDAD ACCION",
    "Aposté a la derrota de EQUIPO.",
    "Puse todo a CUOTA_NUMBER.",
    "Confié en CASA_APUESTAS para este partido.",
    "Metí todo mi bankroll en CRYPTO.",
    "Doble oportunidad para EQUIPO.",
    "JUGADOR está on fire, no podía no apostar.",
    "Vi una cuota CUOTA_NUMBER irresistible.",
    "Cuota de CUOTA_NUMBER demasiado jugosa para dejarla pasar.",
    "Entré fuerte a EQUIPO en CASA_APUESTAS.",
    "Compré más CRYPTO viendo la tendencia.",
    "Golazo de JUGADOR, apuesta ganada.",
    "Aposté a más de CUOTA_CANTIDAD ACCION.",
    "Aposté a menos de CUOTA_CANTIDAD ACCION.",
    "No podía ignorar esa CUOTA_NUMBER en CASA_APUESTAS.",
    "Metí a EQUIPO",
    "Gane la apuesta de CASA_APUESTAS",
    "Aposte al EQUIPO,",
    "CUOTA",
    "CUOTA_CANTIDADEs",
    "Invirtiendo en EQUIPO.",
    "Arriesgué todo en CUOTA_NUMBER.",
    "Deposité mi confianza en JUGADOR.",
    "Probé suerte en CASA_APUESTAS.",
    "Me subí al tren de CRYPTO.",
    "Todo a la victoria de EQUIPO.",
    "Me lancé por esa CUOTA_NUMBER.",
    "Moví todo a CRYPTO sin dudarlo.",
    "Fui con todo por el gol de JUGADOR.",
    "CUOTA_CANTIDAD ACCION cumplido.",
    "Perseguí la remontada de EQUIPO.",
    "Pillé una cuota CUOTA_NUMBER brutal.",
    "Respaldé a EQUIPO en CASA_APUESTAS.",
    "Aumenté posiciones en CRYPTO.",
    "Confiando en el olfato de JUGADOR.",
    "Superando CUOTA_CANTIDAD ACCION fácil.",
    "Reduciendo riesgos a menos de CUOTA_CANTIDAD ACCION.",
    "Encontré un CUOTA_NUMBER que no podía ignorar.",
    "Decidí confiar en CASA_APUESTAS esta vez.",
    "Todo al EQUIPO en este encuentro.",
    "Apoyé a EQUIPO con todo.",
    "Fiché CUOTA_NUMBER sin pensarlo.",
    "Aposté fuerte a más de CUOTA_CANTIDAD ACCION.",
    "Busqué sorpresas con menos de CUOTA_CANTIDAD ACCION.",
    "Metería a EQUIPO",
    "Stakes de CRYPTO"
]

equipos = [
    "Real Madrid", "Barcelona", "Manchester City", "Bayern Munich", "Juventus",
    "Liverpool", "PSG", "Arsenal", "Inter de Milán", "Atlético de Madrid"
]

cuotas = [
    "1.50", "2.00", "2.75", "3.10", "4.50",
    "5.00", "6.25", "7.80", "8.60", "10.00"
]

jugadores = [
    "Messi", "Cristiano Ronaldo", "Haaland", "Mbappé", "Vinícius Jr.",
    "Lewandowski", "Bellingham", "De Bruyne", "Salah", "Griezmann"
]

casas_apuestas = [
    "Bet365", "1xBet", "Betway", "Codere", "Sportium",
    "William Hill", "Pokerstars", "Bwin", "LeoVegas", "888Sport"
]

cryptos = [
    "Bitcoin", "Ethereum", "Dogecoin", "Solana", "Cardano",
    "Ripple", "Shiba Inu", "Polkadot", "Polygon", "Avalanche"
]

acciones = [
    "corners", "penaltis", "amarillas", "faltas"
]


verbos = [
    "aposté", "invertí", "metí", "arriesgué", "puse", "confié", "jugué",
    "entré", "deposité", "probé", "apostaría", "metería", "tiré", "le metí", "apostando"
]

cien = [
    "100", "todo", "mil", "el sueldo", "el bankroll", "la nómina", "mis ahorros"
]

cuota_cantidades = [f"{x:.1f}" for x in [i * 0.5 for i in range(13)]]



variables = {
    "EQUIPO": equipos,
    "JUGADOR": jugadores,
    "CASA_APUESTAS": casas_apuestas,
    "CRYPTO": cryptos,
    "CUOTA_NUMBER": cuotas,
    "CUOTA_CANTIDAD": cuota_cantidades,
    "ACCION": acciones,
    "VERBO": verbos,
    "CIEN": cien
}
def expandir_frases(frases, variables, output_file):
    with open(output_file, "a", encoding="utf-8") as f:
        for frase in frases:
            variables_en_frase = re.findall(r"(EQUIPO|JUGADOR|CASA_APUESTAS|CRYPTO|CUOTA_NUMBER|CUOTA_CANTIDAD|ACCION|VERBO|CIEN)", frase)
            if not variables_en_frase:
                f.write(frase + "\n")
                continue
            listas_de_valores = [variables[var] for var in variables_en_frase]
            for combinacion in itertools.product(*listas_de_valores):
                nueva_frase = frase
                for var, valor in zip(variables_en_frase, combinacion):
                    nueva_frase = nueva_frase.replace(var, valor, 1)
                f.write(nueva_frase + "\n")

expandir_frases(frases, variables, "frases_gambling.txt")
