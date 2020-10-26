# cronlist

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/cronlist) [![Build Status](https://img.shields.io/drone/build/rolehippie/cronlist/master?logo=drone)](https://cloud.drone.io/rolehippie/cronlist) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/cronlist)](https://github.com/rolehippie/cronlist/blob/master/LICENSE) 

Ansible role to install the cronlist executable. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

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

* None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
