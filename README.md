# cronlist

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/cronlist/status.svg)](https://cloud.drone.io/rolehippie/cronlist)

Ansible role to configure cronlist

## Table of content

* [Default Variables](#default-variables)
  * [cronlist_destination](#cronlist_destination)
  * [cronlist_group](#cronlist_group)
  * [cronlist_owner](#cronlist_owner)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

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

## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
