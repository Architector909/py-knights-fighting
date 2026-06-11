def battle(knightsConfig):
    def apply_potion(knight):
        potion = knight["potion"]
        if potion is None:
            return

        effect = potion["effect"]

        knight["hp"] += effect.get("hp", 0)
        knight["power"] += effect.get("power", 0)
        knight["protection"] += effect.get("protection", 0)

    def prepare_knight(knight):
        knight["protection"] = sum(a["protection"] for a in knight["armour"])
        knight["power"] += knight["weapon"]["power"]
        apply_potion(knight)

    knights = {
        name: knight.copy()
        for name, knight in knightsConfig.items()
    }

    for knight in knights.values():
        prepare_knight(knight)

    def fight(a, b):
        a["hp"] -= b["power"] - a["protection"]
        b["hp"] -= a["power"] - b["protection"]

        if a["hp"] < 0:
            a["hp"] = 0
        if b["hp"] < 0:
            b["hp"] = 0

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {
        knight["name"]: knight["hp"]
        for knight in knights.values()
    }
