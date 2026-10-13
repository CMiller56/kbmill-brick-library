# KBMill plant

Spec sheet for the Linux image that ran. Carroll Miller, d/b/a KBMill. 2026-10-10.

## Names

This image is the plant. The package inside the image is `vectorforge_pro`. KBMill and that package are the same vendor.

The image file is `kbmill-plant.tar`. The tag is `kbmill-plant:0.1.0`. The file is 3378268160 bytes. A single-layer DVD-5 holds 4707319808 bytes, so this file fits one DVD. No disc has been burned. This file has not been written as an ISO.

## What the image contains

The image mills a pile into a brick. It includes the local door, the readers, and the weights the mill uses. No chat model is in the image. A customer job does not call a model.

The local door listens on `127.0.0.1:8771`. The drop page takes a pile. `POST /tool/run` takes a name and a path already on the host. One job runs at a time. A second job waits. A finished job can be downloaded from that session. The drop page does not link to the config page.

The license marker `/usr/local/share/kbmill/license.required` is inside the image. The image mills only when a signed plant license names this host. The variable is `VF_PLANT_LICENSE`. When that variable is unset, the file is `/var/lib/kbmill/license.json`.

Docker and Podman both load this file. Nothing is pulled. Podman 3.4 shows the tag as `localhost/kbmill-plant:0.1.0`. The container runs with the network off.

## What the image does not contain

The image does not run the public door, the shelf, or the desk. It does not charge a card. The license private key is not in the image. The operating manual is not in this image. The drop page does not show a Dealt with list.

## The host

One purchase is one host. The host is the fingerprint the image prints, not the hostname. A shelf license does not start the plant. A license for another fingerprint does not start the plant. A missing file does not start the plant.

The fingerprint command, run inside the plant container, is `python3 -m vectorforge_pro.plant_license`. That command prints one line and does not read the license. The buyer sends that line through Contact operator. There is no download URL.

## The brick

The brick file is the handoff. This plant writes it. The desk reads it. The shelf searches it. An unsigned brick still belongs on the shelf. A stale signature still belongs on the shelf.

## What was run

A Linux guest with no copy of the repository loaded this file. Docker and Podman each printed the same fingerprint, with the network off. With no license, both refused. With a shelf license, the plant refused. With a plant license for that guest, Docker took two drops. The second drop waited, and both became bricks. A tool call on Docker milled a brick. A tool call on Podman milled a brick. Each receipt showed no model turn. Nothing was fetched. The private key was not on that guest.

The guest's older plant door was left running. That door is a different image. Loading this file did not replace it.
