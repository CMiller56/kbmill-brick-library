# KBMill Desktop

Spec sheet for the Linux image that ran. Carroll Miller, d/b/a KBMill. 2026-10-10.

## Names

The window is KBMill Desktop. The package inside the image is `vectorforge_pro`. KBMill and that package are the same vendor.

The image file is `kbmill-desk.tar`. The tag is `kbmill-desk:0.1.0`. The file is 114298880 bytes. A single-layer DVD-5 holds 4707319808 bytes, so this file fits one DVD. No disc has been burned.

## What the image contains

The image opens a finished brick, marks a chunk seen, edits a chunk, mutes a chunk, and signs the brick. The operating manual is in the image at `/usr/local/share/kbmill/MANUAL.md`. The image can open that file as the brick KBMill_Manual.

Inside the image the desk listens on `127.0.0.1:8766`. The calls are `POST /brick/open`, `POST /brick/seen`, `POST /brick/commit`, and `POST /brick/sign`. `GET /` returns the window title and the listen address.

The license marker `/usr/local/share/kbmill/license.required` is inside the image. The image asks for an auditor license that names this host. The variable is `VF_AUDIT_LICENSE`. When that variable is unset, the file is `/var/lib/kbmill/license.json`.

Docker and Podman both load this file. Nothing is pulled. Podman 3.4 shows the tag as `localhost/kbmill-desk:0.1.0`. The container runs with the network off.

## What the image does not contain

The image does not run the mill. It does not run the public door, the shelf server, or a chat model. It does not charge a card. The license private key is not in the image. `link_bricks` is not a route on this desk.

## The host

One purchase is one host. The host is the fingerprint the image prints, not the hostname. A plant license does not start the desk. A shelf license does not start the desk. A license for another fingerprint does not start the desk. A missing file does not start the desk.

The fingerprint command, run inside the container, is `python3 -m vectorforge_pro.plant_license`. That command prints one line and does not read the license. The buyer sends that line through Contact operator. There is no download URL.

## The brick

The brick file is the handoff. The plant writes it. This desk reads it, and a person may edit it and sign it. Signing does not put the brick on the shelf. An unsigned brick still belongs on the shelf. A stale signature still belongs on the shelf.

## What was run

A Linux guest with no copy of the repository loaded this file. Docker and Podman each ran it with the network off. With no license, both refused. With a plant license, both refused. With an auditor license for that guest, both opened a zip brick, marked one chunk seen, and signed it. Opening it again matched. Nothing was fetched. The private key was not on that guest.

The screen control that opens a zip by path is not on the window yet. The image answers the calls above. Do not describe a button that is not on the screen.
