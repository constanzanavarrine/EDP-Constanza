from typing import Callable, List, Optional

from anfibio import Anfibio
from auto import Auto
from camion import Camion
from lancha import Lancha
from registro_patentes import RegistroPatentes
from vehiculo import Vehiculo
from velero import Velero


def registrar_vehiculo(
    creador: Callable[[], Vehiculo],
    descripcion: str,
    flota: List[Vehiculo],
) -> Optional[Vehiculo]:
    try:
        vehiculo = creador()
    except ValueError as error:
        print(f"[ERROR] {descripcion}: {error}")
        return None
    else:
        flota.append(vehiculo)
        print(f"[OK] {descripcion} registrado con patente {vehiculo.patente}.")
        return vehiculo


def main() -> None:
    RegistroPatentes.configurar_prefijo("terrestre", "TER")
    RegistroPatentes.configurar_prefijo("acuatico", "ACU")

    flota: List[Vehiculo] = []

    auto1 = registrar_vehiculo(
        lambda: Auto(marca="Ford", anio=2020),
        "Auto Ford 2020",
        flota,
    )

    if auto1 is not None:
        registrar_vehiculo(
            lambda: Camion(
                patente=auto1.patente,
                marca="Volvo",
                anio=2018,
                capacidad_carga=18.5,
            ),
            "Camion Volvo 2018 con patente repetida",
            flota,
        )

    registrar_vehiculo(
        lambda: Lancha(
            patente=auto1.patente if auto1 else None,
            marca="Yamaha",
            anio=2021,
            marca_motor="Mercury",
        ),
        "Lancha Yamaha 2021 con patente compartida con terrestre",
        flota,
    )

    registrar_vehiculo(
        lambda: Velero(marca="Beneteau", anio=2019, cantidad_velas=3),
        "Velero Beneteau 2019",
        flota,
    )

    registrar_vehiculo(
        lambda: Anfibio(marca="Gibbs", modelo="Quadski"),
        "Anfibio Gibbs Quadski",
        flota,
    )

    print("\nResumen de la flota generada:")
    for vehiculo in flota:
        try:
            mensaje = vehiculo.trasladarse(5)
        except NotImplementedError as error:
            print(f" - {vehiculo.__class__.__name__}: no implemento traslado ({error}).")
        else:
            print(
                f" - {vehiculo.__class__.__name__} patente {vehiculo.patente}: {mensaje}"
            )


if __name__ == "__main__":
    main()
