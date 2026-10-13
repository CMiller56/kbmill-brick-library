# KBMill shelf

Spec sheet for the Linux image that ran. Carroll Miller, d/b/a KBMill. 2026-10-10.

## Names

This image is the shelf. The Constructor is this shelf. The package inside the image is `vectorforge_pro`. KBMill and that package are the same vendor.

The image file is `kbmill-shelf.tar`. The tag is `kbmill-shelf:0.1.0`. The file is 1966346240 bytes. A single-layer DVD-5 holds 4707319808 bytes, so this file fits one DVD. No disc has been burned. This file has not been written as an ISO.

## What the image contains

The image answers a question from bricks it has been given. It does not mill, and it does not edit a brick. No chat model is in the image. The question is embedded with the weights in the image.

The baked config is `/usr/local/share/kbmill/shelf.json`. The library folder is `/library`. The listen address is `127.0.0.1:8772`. A model calls the shelf at `/mcp` on that door. The tools are `list_shelf`, `open_set`, and `search_shelf`. `list_shelf` reads the card. `open_set` chooses at most 3 bricks by default, and 4 at the hard stop. `search_shelf` returns cites from those bricks. A muted chunk stays out of the cites. `link_bricks` is not a tool.

`GET /status` reports the library folder, whether the card is loaded, and the counts. It does not return a passage. There is no drop page and no config page. The tool call has no password.

The catalog is written from inside the image. On the baked library path the command is `python3 -m vectorforge_pro.indexer build /library`. That writes `catalog.json` and `CATALOG.md` in `/library`. A later batch uses `python3 -m vectorforge_pro.indexer update`. The shelf server does not build the catalog by itself.

The license marker `/usr/local/share/kbmill/license.required` is inside the image. The image listens only when a signed shelf license names this host. The variable is `VF_SHELF_LICENSE`. When that variable is unset, the file is `/var/lib/kbmill/license.json`.

Docker and Podman both load this file. Nothing is pulled. Podman 3.4 shows the tag as `localhost/kbmill-shelf:0.1.0`. The container runs with the network off.

## What the image does not contain

The image does not run the mill, the desk, or the public door. It does not charge a card. The license private key is not in the image. The operating manual is not in this image. There is no upload route.

## The host

One purchase is one host. The host is the fingerprint the image prints, not the hostname. A plant license does not start the shelf. A desk license does not start the shelf. A license for another fingerprint does not start the shelf. A missing file does not start the shelf.

The fingerprint command, run inside the shelf container, is `python3 -m vectorforge_pro.plant_license`. That command prints one line and does not read the license. The buyer sends that line through Contact operator. There is no download URL.

## The brick

The brick file is the handoff. The plant writes it. This shelf searches it. The desk may edit it and sign it. An unsigned brick still belongs on the shelf. A stale signature still belongs on the shelf. Copying a brick into the library folder does not put it on the card until the catalog is built from inside this image.

## What was run

A Linux guest with no copy of the repository loaded this file. Docker and Podman each ran it with the network off. With no license, both refused. With a plant license, both refused. With a shelf license for that guest, both listed the card, chose a brick, and returned cites from that brick. `link_bricks` was refused. The weights in the image embedded the question. Nothing was fetched. The private key was not on that guest.

The guest's plant door was left running. Loading this file did not replace it.
