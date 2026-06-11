from typing import Dict, Any


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:

    def apply_potion(knight: Dict[str, Any]) -> None:
        potion = knight["potion"]
        if potion is None:
            return

        effect = potion["effect"]

        knight["hp"] += effect.get("hp", 0)
        knight["power"] += effect.get("power", 0)
        knight["protection"] += effect.get("protection", 0)

    def prepare_knight(knight: Dict[str, Any]) -> None:
        knight["protection"] = sum(a["protection"] for a in knight["armour"])
        knight["power"] += knight["weapon"]["power"]
        apply_potion(knight)

    knights = {
        name: knight.copy()
        for name, knight in knights_config.items()
    }

    for knight in knights.values():
        prepare_knight(knight)

    def fight(attacker: Dict[str, Any], defender: Dict[str, Any]) -> None:
        defender["hp"] -= attacker["power"] - defender["protection"]
        attacker["hp"] -= defender["power"] - attacker["protection"]

        if attacker["hp"] < 0:
            attacker["hp"] = 0
        if defender["hp"] < 0:
            defender["hp"] = 0

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        knight["name"]: knight["hp"]
        for knight in knights.values()
    }
