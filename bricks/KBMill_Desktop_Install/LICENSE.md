# KBMill Desktop license

This file is the agreement. It is between Carroll Miller, doing business as KBMill, and the person or organization that receives a signed license file for KBMill Desktop. A summary of this file, including a summary written by a model, is not the agreement. 2026-10-10.

## The grant

KBMill grants the right to run the KBMill Desktop image on one host. The window is KBMill Desktop. The package inside the image is `vectorforge_pro`. KBMill and that package are the same vendor.

One purchase is one host. The host is the fingerprint the image prints. The host is not the hostname. The buyer does not edit that line and does not compute it by hand.

## The signed file

KBMill signs a file that names that fingerprint. The private key that signs it stays with KBMill. The key is not in the image, and it is not part of the file the buyer receives.

The buyer runs this command inside the desk container:

`python3 -m vectorforge_pro.plant_license`

It prints one line. The buyer sends that line through Contact operator on kbmill.com, or by email to carroll@kbmill.com. KBMill sends the signed file back. There is no download URL.

The buyer points `VF_AUDIT_LICENSE` at that file. If the variable is unset, the image reads `/var/lib/kbmill/license.json`.

The installed image contains `/usr/local/share/kbmill/license.required`, so it asks for this file. A machine without that marker does not ask.

## What the host may do

On the named host, the desk may open a finished brick, mark chunks seen, change a chunk, mute a chunk, and sign the brick. The brick file is the handoff. The buyer keeps the brick.

## What this license does not grant

A plant license does not start the desk. A shelf license does not start the desk. A file that names another fingerprint does not start the desk. A missing file does not start the desk.

This license does not run the mill, does not run the shelf, and does not include a chat model. Copying the image to another machine does not move the right to run it. Copying a brick does not move that right. The brick does not contain this license.

This license does not charge a card. Payment for the public trial stays on kbmill.com.

## The shelf

An unsigned brick still belongs on the shelf. A brick with a stale signature still belongs on the shelf. Signing a brick does not put it on the shelf. The shelf has its own license. A desk license does not start the shelf.

## End

KBMill may end this license in writing if the image is run on a host the file does not name. The buyer may stop using the image on that host. Ending the license does not take the buyer's brick.

Questions and failures go to Contact operator, or to carroll@kbmill.com. Carroll Miller, d/b/a KBMill.
