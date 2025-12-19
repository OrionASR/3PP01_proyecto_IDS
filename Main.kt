package cososKotlin

fun main() {
    val gifts = mutableListOf<Gift>(
        Gift("car", 3),
        Gift("doll", 1),
        Gift("ball", 2),
        Gift("train", 0),
        Gift("bear", -2),
        Gift("puzzle", 1)
    )

    val fixed_gifts = mutableListOf<Gift>()

    for (i in 0 until gifts.size) {
        if (gifts[i].cantidad > 0) fixed_gifts.add(gifts[i])
    }

    for (i in 0 until fixed_gifts.size) {
        println("${fixed_gifts[i].nombre}: ${fixed_gifts[i].cantidad} unidades")
    }

    //pepe
}
