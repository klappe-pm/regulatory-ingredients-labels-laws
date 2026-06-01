# environment-macos-machine-specs

## System Context
This machine is a MacBook Pro (2023, Mac15,7) running macOS 15.6.1 (Sequoia). Use these specifications when making recommendations about software installation, performance optimization, or system compatibility.

## Hardware Specifications

### Processor
- **CPU**: Apple M3 Pro (ARM64 architecture)
- **Cores**: 12 total (6 performance + 6 efficiency)
- **Performance Profile**: High-performance workstation suitable for intensive development, compilation, virtualization, and AI/ML workloads

### Memory
- **RAM**: 36 GB unified memory
- **Memory Architecture**: Unified memory shared between CPU and GPU
- **Capacity Assessment**: Excellent for multi-tasking, large-scale development, containers, and memory-intensive applications

### Graphics
- **GPU**: Apple M3 Pro integrated GPU
- **GPU Cores**: 18 cores
- **Graphics API**: Metal 3 support
- **Use Cases**: Suitable for GPU-accelerated workloads, machine learning, video processing, and graphics development

### Storage
- **Drive**: APPLE SSD AP0512Z (512 GB internal SSD)
- **Available Space**: 182 GB free (out of 494 GB usable)
- **File System**: APFS
- **Protocol**: Apple Fabric (high-performance interconnect)
- **Performance**: NVMe-class SSD with excellent read/write speeds

### Display
- **Type**: Built-in Liquid Retina XDR Display
- **Resolution**: 3456 x 2234 (Retina quality)
- **Capabilities**: HDR support, high color accuracy

## Software Environment

### Operating System
- **OS**: macOS 15.6.1 (Sequoia)
- **Kernel**: Darwin 24.6.0
- **Architecture**: ARM64 (Apple Silicon)
- **Security**: SIP enabled, Secure Virtual Memory enabled

### Compatibility Considerations
- **Native Support**: ARM64/Apple Silicon native applications preferred for best performance
- **Rosetta 2**: Available for x86_64 compatibility when needed
- **Homebrew**: Use `/opt/homebrew` prefix (ARM64 native)
- **Docker**: Supports ARM64 containers natively; x86_64 via emulation
- **Programming Languages**: Most modern languages have ARM64 native builds (Python, Node.js, Go, Rust, etc.)

## Performance Characteristics

### Strengths
- Excellent single-core and multi-core CPU performance
- High memory bandwidth due to unified architecture
- Fast SSD with low latency
- Efficient power management and thermal handling
- Strong GPU performance for integrated graphics

### Optimal Workloads
- Software development (all major languages and IDEs)
- Containerization and virtualization (Docker, Podman, UTM)
- Web development and local server hosting
- Machine learning inference and training (moderate scale)
- Video/audio processing and editing
- Large-scale data processing and analysis
- Multiple concurrent development environments

### Resource Availability
- **CPU**: 12 cores available for parallel processing
- **Memory**: 36 GB allows for extensive multi-tasking without swap pressure
- **Storage**: 182 GB free for projects, dependencies, and development tools
- **Network**: Multiple network adapters available

## Recommendations for AI Assistants

When providing technical guidance for this system:

1. **Package Installation**: Prefer Homebrew (`brew install`) for macOS-native installations
2. **Architecture**: Recommend ARM64-native versions when available; note when Rosetta 2 compatibility is required
3. **Resource Allocation**: Can safely allocate significant resources (e.g., Docker memory limits up to 16-20 GB, multiple concurrent services)
4. **Performance Expectations**: Set expectations for fast compilation times, quick build processes, and responsive development environments
5. **Storage Management**: Monitor disk usage but 182 GB provides comfortable headroom for most development projects
6. **Compatibility**: Check for Apple Silicon compatibility for specialized tools; most modern development tools are well-supported

## Working Directory
- **Current Directory**: /Users/kevinlappe
- **User**: kevinlappe (Kevin Lappe)
- **Home Directory**: Standard macOS user home directory structure

## System Health
- **Uptime**: Stable (22+ hours since last boot)
- **SSD Health**: Verified (S.M.A.R.T. status good)
- **Security Posture**: Strong (SIP enabled, secure boot, firmware up to date)
- **Disk Usage**: Healthy (6% capacity used, no immediate storage concerns)
