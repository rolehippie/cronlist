# cronlist

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/cronlist) [![Testing Build](https://github.com/rolehippie/cronlist/workflows/testing/badge.svg)](https://github.com/rolehippie/cronlist/actions?query=workflow%3Atesting) [![Readme Build](https://github.com/rolehippie/cronlist/workflows/readme/badge.svg)](https://github.com/rolehippie/cronlist/actions?query=workflow%3Areadme) [![Galaxy Build](https://github.com/rolehippie/cronlist/workflows/galaxy/badge.svg)](https://github.com/rolehippie/cronlist/actions?query=workflow%3Agalaxy) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/cronlist)](https://github.com/rolehippie/cronlist/blob/master/LICENSE)

Ansible role to install the cronlist executable.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Default Variables](#default-variables)
  - [cronlist_destination](#cronlist_destination)
  - [cronlist_group](#cronlist_group)
  - [cronlist_owner](#cronlist_owner)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Default Variables

### cronlist_destination

Destination for executable

#### Default value

```YAML
cronlist_destination: /usr/bin/cronlist
```

### cronlist_group

Group for the executable

#### Default value

```YAML
cronlist_group: root
```

### cronlist_owner

User for the executable

#### Default value

```YAML
cronlist_owner: root
```

## Discovered Tags

**_cronlist_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
