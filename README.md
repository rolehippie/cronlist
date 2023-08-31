# cronlist

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/cronlist)
[![General Workflow](https://github.com/rolehippie/cronlist/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/cronlist/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/cronlist/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/cronlist/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/cronlist/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/cronlist/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/cronlist)](https://github.com/rolehippie/cronlist/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.cronlist-blue)](https://galaxy.ansible.com/rolehippie/cronlist)

Ansible role to install the cronlist executable.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [cronlist_destination](#cronlist_destination)
  - [cronlist_group](#cronlist_group)
  - [cronlist_owner](#cronlist_owner)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`

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
