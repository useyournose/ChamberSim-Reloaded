local admonition_titles = {
  warning = "Safety",
  note = "Note",
}

function Image(image)
  if not image.src:match("^[%a][%w+.-]*:") and
     not image.src:match("^/") and
     not image.src:match("^images/") then
    image.src = "images/" .. image.src
  end
  return image
end

function Table(table)
  return pandoc.RawBlock(
    "markdown",
    pandoc.write(pandoc.Pandoc({table}), "gfm")
  )
end

function Div(div)
  for class, title in pairs(admonition_titles) do
    if div.classes:includes(class) then
      local markdown = pandoc.write(pandoc.Pandoc(div.content), "markdown")
      local indented = markdown:gsub("([^\n]+)", "    %1")
      return pandoc.RawBlock(
        "markdown",
        '!!! ' .. class .. ' "' .. title .. '"\n\n' .. indented
      )
    end
  end

  if div.classes:includes("center") then
    return div.content
  end
end
