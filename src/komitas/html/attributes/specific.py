from __future__ import annotations

from .base import Attribute

__all__ = [
    "HTMLAttribute",
    "AAttribute",
    "AreaAttribute",
    "AudioAttribute",
    "BackgroundImageAttribute",
    "BaseAttribute",
    "BlockquoteAttribute",
    "BodyAttribute",
    "ButtonAttribute",
    "CanvasAttribute",
    "CaptionAttribute",
    "ColAttribute",
    "ColgroupAttribute",
    "DataAttribute",
    "DelAttribute",
    "DetailsAttribute",
    "DialogAttribute",
    "EmbedAttribute",
    "FieldsetAttribute",
    "FontAttribute",
    "FormAttribute",
    "HrAttribute",
    "IframeAttribute",
    "ImageAttribute",
    "ImgAttribute",
    "InputAttribute",
    "InsAttribute",
    "LabelAttribute",
    "LiAttribute",
    "LinkAttribute",
    "MapAttribute",
    "MarqueeAttribute",
    "MenuAttribute",
    "MetaAttribute",
    "MeterAttribute",
    "ObjectAttribute",
    "OlAttribute",
    "OptgroupAttribute",
    "OptionAttribute",
    "OutputAttribute",
    "PAttribute",
    "ParamAttribute",
    "ProgressAttribute",
    "QAttribute",
    "ScriptAttribute",
    "SelectAttribute",
    "SourceAttribute",
    "StyleAttribute",
    "SvgAttribute",
    "TableAttribute",
    "TbodyAttribute",
    "TdAttribute",
    "TextareaAttribute",
    "TfootAttribute",
    "ThAttribute",
    "TheadAttribute",
    "TimeAttribute",
    "TrAttribute",
    "TrackAttribute",
    "VideoAttribute",
    "Accept",
    "AcceptCharset",
    "Action",
    "Align",
    "Allow",
    "Alpha",
    "Alt",
    "As",
    "Async",
    "Autocomplete",
    "Autoplay",
    "Background",
    "Bgcolor",
    "Border",
    "Capture",
    "Charset",
    "Checked",
    "Cite",
    "Color",
    "Colorspace",
    "Cols",
    "Colspan",
    "Content",
    "Controls",
    "Coords",
    "Crossorigin",
    "Csp",
    "Data",
    "Datetime",
    "Decoding",
    "Default",
    "Defer",
    "Dirname",
    "Disabled",
    "Download",
    "Elementtiming",
    "Enctype",
    "For",
    "Form",
    "Formaction",
    "Formenctype",
    "Formmethod",
    "Formnovalidate",
    "Formtarget",
    "Headers",
    "Height",
    "High",
    "Href",
    "Hreflang",
    "HttpEquiv",
    "Integrity",
    "Ismap",
    "Kind",
    "Label",
    "Language",
    "List",
    "Loading",
    "Loop",
    "Low",
    "Manifest",
    "Max",
    "Maxlength",
    "Media",
    "Method",
    "Min",
    "Minlength",
    "Multiple",
    "Muted",
    "Name",
    "Novalidate",
    "Open",
    "Optimum",
    "Pattern",
    "Ping",
    "Placeholder",
    "Playsinline",
    "Poster",
    "Preload",
    "Readonly",
    "Referrerpolicy",
    "Rel",
    "Required",
    "Reversed",
    "Rows",
    "Rowspan",
    "Sandbox",
    "Scope",
    "Selected",
    "Shape",
    "Size",
    "Sizes",
    "SpanAttr",
    "Src",
    "Srcdoc",
    "Srclang",
    "Srcset",
    "Start",
    "Step",
    "Summary",
    "Target",
    "Type",
    "Usemap",
    "Value",
    "Version",
    "Width",
    "Wrap",
    "Xmlns",
    "get_tag_attribute_mixins"
]

class HTMLAttribute(Attribute):
    """Attributes specific to the <html> element."""

    pass

class AAttribute(Attribute):
    pass

class AreaAttribute(Attribute):
    pass

class AudioAttribute(Attribute):
    pass

class BackgroundImageAttribute(Attribute):
    pass

class BaseAttribute(Attribute):
    pass

class BlockquoteAttribute(Attribute):
    pass

class BodyAttribute(Attribute):
    pass

class ButtonAttribute(Attribute):
    pass

class CanvasAttribute(Attribute):
    pass

class CaptionAttribute(Attribute):
    pass

class ColAttribute(Attribute):
    pass

class ColgroupAttribute(Attribute):
    pass

class DataAttribute(Attribute):
    pass

class DelAttribute(Attribute):
    pass

class DetailsAttribute(Attribute):
    pass

class DialogAttribute(Attribute):
    pass

class EmbedAttribute(Attribute):
    pass

class FieldsetAttribute(Attribute):
    pass

class FontAttribute(Attribute):
    pass

class FormAttribute(Attribute):
    pass

class HrAttribute(Attribute):
    pass

class IframeAttribute(Attribute):
    pass

class ImageAttribute(Attribute):
    pass

class ImgAttribute(Attribute):
    pass

class InputAttribute(Attribute):
    pass

class InsAttribute(Attribute):
    pass

class LabelAttribute(Attribute):
    pass

class LiAttribute(Attribute):
    pass

class LinkAttribute(Attribute):
    pass

class MapAttribute(Attribute):
    pass

class MarqueeAttribute(Attribute):
    pass

class MenuAttribute(Attribute):
    pass

class MetaAttribute(Attribute):
    pass

class MeterAttribute(Attribute):
    pass

class ObjectAttribute(Attribute):
    pass

class OlAttribute(Attribute):
    pass

class OptgroupAttribute(Attribute):
    pass

class OptionAttribute(Attribute):
    pass

class OutputAttribute(Attribute):
    pass

class PAttribute(Attribute):
    pass

class ParamAttribute(Attribute):
    pass

class ProgressAttribute(Attribute):
    pass

class QAttribute(Attribute):
    pass

class ScriptAttribute(Attribute):
    pass

class SelectAttribute(Attribute):
    pass

class SourceAttribute(Attribute):
    pass

class StyleAttribute(Attribute):
    pass

class SvgAttribute(Attribute):
    pass

class TableAttribute(Attribute):
    pass

class TbodyAttribute(Attribute):
    pass

class TdAttribute(Attribute):
    pass

class TextareaAttribute(Attribute):
    pass

class TfootAttribute(Attribute):
    pass

class ThAttribute(Attribute):
    pass

class TheadAttribute(Attribute):
    pass

class TimeAttribute(Attribute):
    pass

class TrAttribute(Attribute):
    pass

class TrackAttribute(Attribute):
    pass

class VideoAttribute(Attribute):
    pass

class Accept(FormAttribute, InputAttribute):
    attribute_name = "accept"

class AcceptCharset(FormAttribute):
    attribute_name = "accept-charset"

class Action(FormAttribute):
    attribute_name = "action"

class Align(CaptionAttribute, ColAttribute, ColgroupAttribute, HrAttribute, IframeAttribute, ImgAttribute, TableAttribute, TbodyAttribute, TdAttribute, TfootAttribute, ThAttribute, TheadAttribute, TrAttribute):
    attribute_name = "align"

class Allow(IframeAttribute):
    attribute_name = "allow"

class Alpha(InputAttribute):
    attribute_name = "alpha"

class Alt(AreaAttribute, ImgAttribute, InputAttribute):
    attribute_name = "alt"

class As(LinkAttribute):
    attribute_name = "as"

class Async(ScriptAttribute):
    attribute_name = "async"

class Autocomplete(FormAttribute, InputAttribute, SelectAttribute, TextareaAttribute):
    attribute_name = "autocomplete"

class Autoplay(AudioAttribute, VideoAttribute):
    attribute_name = "autoplay"

class Background(BodyAttribute, TableAttribute, TdAttribute, ThAttribute):
    attribute_name = "background"

class Bgcolor(BodyAttribute, ColAttribute, ColgroupAttribute, MarqueeAttribute, TableAttribute, TbodyAttribute, TfootAttribute, TdAttribute, ThAttribute, TrAttribute):
    attribute_name = "bgcolor"

class Border(ImgAttribute, ObjectAttribute, TableAttribute):
    attribute_name = "border"

class Capture(InputAttribute):
    attribute_name = "capture"

class Charset(MetaAttribute):
    attribute_name = "charset"

class Checked(InputAttribute):
    attribute_name = "checked"

class Cite(BlockquoteAttribute, DelAttribute, InsAttribute, QAttribute):
    attribute_name = "cite"

class Color(FontAttribute, HrAttribute):
    attribute_name = "color"

class Colorspace(InputAttribute):
    attribute_name = "colorspace"

class Cols(TextareaAttribute):
    attribute_name = "cols"

class Colspan(TdAttribute, ThAttribute):
    attribute_name = "colspan"

class Content(MetaAttribute):
    attribute_name = "content"

class Controls(AudioAttribute, VideoAttribute):
    attribute_name = "controls"

class Coords(AreaAttribute):
    attribute_name = "coords"

class Crossorigin(AudioAttribute, ImgAttribute, LinkAttribute, ScriptAttribute, VideoAttribute):
    attribute_name = "crossorigin"

class Csp(IframeAttribute):
    attribute_name = "csp"

class Data(ObjectAttribute):
    attribute_name = "data"

class Datetime(DelAttribute, InsAttribute, TimeAttribute):
    attribute_name = "datetime"

class Decoding(ImgAttribute):
    attribute_name = "decoding"

class Default(TrackAttribute):
    attribute_name = "default"

class Defer(ScriptAttribute):
    attribute_name = "defer"

class Dirname(InputAttribute, TextareaAttribute):
    attribute_name = "dirname"

class Disabled(ButtonAttribute, FieldsetAttribute, InputAttribute, OptgroupAttribute, OptionAttribute, SelectAttribute, TextareaAttribute):
    attribute_name = "disabled"

class Download(AAttribute, AreaAttribute):
    attribute_name = "download"

class Elementtiming(ImgAttribute, ImageAttribute, SvgAttribute, VideoAttribute, BackgroundImageAttribute, PAttribute):
    attribute_name = "elementtiming"

class Enctype(FormAttribute):
    attribute_name = "enctype"

class For(LabelAttribute, OutputAttribute):
    attribute_name = "for"

class Form(ButtonAttribute, FieldsetAttribute, InputAttribute, ObjectAttribute, OutputAttribute, SelectAttribute, TextareaAttribute):
    attribute_name = "form"

class Formaction(InputAttribute, ButtonAttribute):
    attribute_name = "formaction"

class Formenctype(ButtonAttribute, InputAttribute):
    attribute_name = "formenctype"

class Formmethod(ButtonAttribute, InputAttribute):
    attribute_name = "formmethod"

class Formnovalidate(ButtonAttribute, InputAttribute):
    attribute_name = "formnovalidate"

class Formtarget(ButtonAttribute, InputAttribute):
    attribute_name = "formtarget"

class Headers(TdAttribute, ThAttribute):
    attribute_name = "headers"

class Height(CanvasAttribute, EmbedAttribute, IframeAttribute, ImgAttribute, InputAttribute, ObjectAttribute, VideoAttribute):
    attribute_name = "height"

class High(MeterAttribute):
    attribute_name = "high"

class Href(AAttribute, AreaAttribute, BaseAttribute, LinkAttribute):
    attribute_name = "href"

class Hreflang(AAttribute, LinkAttribute):
    attribute_name = "hreflang"

class HttpEquiv(MetaAttribute):
    attribute_name = "http-equiv"

class Integrity(LinkAttribute, ScriptAttribute):
    attribute_name = "integrity"

class Ismap(ImgAttribute):
    attribute_name = "ismap"

class Kind(TrackAttribute):
    attribute_name = "kind"

class Label(OptgroupAttribute, OptionAttribute, TrackAttribute):
    attribute_name = "label"

class Language(ScriptAttribute):
    attribute_name = "language"

class List(InputAttribute):
    attribute_name = "list"

class Loading(ImgAttribute, IframeAttribute):
    attribute_name = "loading"

class Loop(AudioAttribute, MarqueeAttribute, VideoAttribute):
    attribute_name = "loop"

class Low(MeterAttribute):
    attribute_name = "low"

class Manifest(HTMLAttribute):
    attribute_name = "manifest"

class Max(InputAttribute, MeterAttribute, ProgressAttribute):
    attribute_name = "max"

class Maxlength(InputAttribute, TextareaAttribute):
    attribute_name = "maxlength"

class Media(AAttribute, AreaAttribute, LinkAttribute, SourceAttribute, StyleAttribute):
    attribute_name = "media"

class Method(FormAttribute):
    attribute_name = "method"

class Min(InputAttribute, MeterAttribute):
    attribute_name = "min"

class Minlength(InputAttribute, TextareaAttribute):
    attribute_name = "minlength"

class Multiple(InputAttribute, SelectAttribute):
    attribute_name = "multiple"

class Muted(AudioAttribute, VideoAttribute):
    attribute_name = "muted"

class Name(ButtonAttribute, FormAttribute, FieldsetAttribute, IframeAttribute, InputAttribute, ObjectAttribute, OutputAttribute, SelectAttribute, TextareaAttribute, MapAttribute, MetaAttribute, ParamAttribute):
    attribute_name = "name"

class Novalidate(FormAttribute):
    attribute_name = "novalidate"

class Open(DetailsAttribute, DialogAttribute):
    attribute_name = "open"

class Optimum(MeterAttribute):
    attribute_name = "optimum"

class Pattern(InputAttribute):
    attribute_name = "pattern"

class Ping(AAttribute, AreaAttribute):
    attribute_name = "ping"

class Placeholder(InputAttribute, TextareaAttribute):
    attribute_name = "placeholder"

class Playsinline(VideoAttribute):
    attribute_name = "playsinline"

class Poster(VideoAttribute):
    attribute_name = "poster"

class Preload(AudioAttribute, VideoAttribute):
    attribute_name = "preload"

class Readonly(InputAttribute, TextareaAttribute):
    attribute_name = "readonly"

class Referrerpolicy(AAttribute, AreaAttribute, IframeAttribute, ImgAttribute, LinkAttribute, ScriptAttribute):
    attribute_name = "referrerpolicy"

class Rel(AAttribute, AreaAttribute, LinkAttribute):
    attribute_name = "rel"

class Required(InputAttribute, SelectAttribute, TextareaAttribute):
    attribute_name = "required"

class Reversed(OlAttribute):
    attribute_name = "reversed"

class Rows(TextareaAttribute):
    attribute_name = "rows"

class Rowspan(TdAttribute, ThAttribute):
    attribute_name = "rowspan"

class Sandbox(IframeAttribute):
    attribute_name = "sandbox"

class Scope(ThAttribute):
    attribute_name = "scope"

class Selected(OptionAttribute):
    attribute_name = "selected"

class Shape(AAttribute, AreaAttribute):
    attribute_name = "shape"

class Size(InputAttribute, SelectAttribute):
    attribute_name = "size"

class Sizes(LinkAttribute, ImgAttribute, SourceAttribute):
    attribute_name = "sizes"

class SpanAttr(ColAttribute, ColgroupAttribute):
    attribute_name = "span"

class Src(AudioAttribute, EmbedAttribute, IframeAttribute, ImgAttribute, InputAttribute, ScriptAttribute, SourceAttribute, TrackAttribute, VideoAttribute):
    attribute_name = "src"

class Srcdoc(IframeAttribute):
    attribute_name = "srcdoc"

class Srclang(TrackAttribute):
    attribute_name = "srclang"

class Srcset(ImgAttribute, SourceAttribute):
    attribute_name = "srcset"

class Start(OlAttribute):
    attribute_name = "start"

class Step(InputAttribute):
    attribute_name = "step"

class Summary(TableAttribute):
    attribute_name = "summary"

class Target(AAttribute, AreaAttribute, BaseAttribute, FormAttribute):
    attribute_name = "target"

class Type(ButtonAttribute, InputAttribute, EmbedAttribute, ObjectAttribute, OlAttribute, ScriptAttribute, SourceAttribute, StyleAttribute, MenuAttribute, LinkAttribute):
    attribute_name = "type"

class Usemap(ImgAttribute, InputAttribute, ObjectAttribute):
    attribute_name = "usemap"

class Value(ButtonAttribute, DataAttribute, InputAttribute, LiAttribute, MeterAttribute, OptionAttribute, ProgressAttribute, ParamAttribute):
    attribute_name = "value"

class Version(HTMLAttribute):
    attribute_name = "version"

class Width(CanvasAttribute, EmbedAttribute, IframeAttribute, ImgAttribute, InputAttribute, ObjectAttribute, VideoAttribute):
    attribute_name = "width"

class Wrap(TextareaAttribute):
    attribute_name = "wrap"

class Xmlns(HTMLAttribute):
    attribute_name = "xmlns"

TAG_ATTRIBUTE_MIXINS = {
    "a": AAttribute,
    "area": AreaAttribute,
    "audio": AudioAttribute,
    "background-image": BackgroundImageAttribute,
    "base": BaseAttribute,
    "blockquote": BlockquoteAttribute,
    "body": BodyAttribute,
    "button": ButtonAttribute,
    "canvas": CanvasAttribute,
    "caption": CaptionAttribute,
    "col": ColAttribute,
    "colgroup": ColgroupAttribute,
    "data": DataAttribute,
    "del": DelAttribute,
    "details": DetailsAttribute,
    "dialog": DialogAttribute,
    "embed": EmbedAttribute,
    "fieldset": FieldsetAttribute,
    "font": FontAttribute,
    "form": FormAttribute,
    "hr": HrAttribute,
    "html": HTMLAttribute,
    "iframe": IframeAttribute,
    "image": ImageAttribute,
    "img": ImgAttribute,
    "input": InputAttribute,
    "ins": InsAttribute,
    "label": LabelAttribute,
    "li": LiAttribute,
    "link": LinkAttribute,
    "map": MapAttribute,
    "marquee": MarqueeAttribute,
    "menu": MenuAttribute,
    "meta": MetaAttribute,
    "meter": MeterAttribute,
    "object": ObjectAttribute,
    "ol": OlAttribute,
    "optgroup": OptgroupAttribute,
    "option": OptionAttribute,
    "output": OutputAttribute,
    "p": PAttribute,
    "param": ParamAttribute,
    "progress": ProgressAttribute,
    "q": QAttribute,
    "script": ScriptAttribute,
    "select": SelectAttribute,
    "source": SourceAttribute,
    "style": StyleAttribute,
    "svg": SvgAttribute,
    "table": TableAttribute,
    "tbody": TbodyAttribute,
    "td": TdAttribute,
    "textarea": TextareaAttribute,
    "tfoot": TfootAttribute,
    "th": ThAttribute,
    "thead": TheadAttribute,
    "time": TimeAttribute,
    "tr": TrAttribute,
    "track": TrackAttribute,
    "video": VideoAttribute,
}

def get_tag_attribute_mixins(tag_name: str):
    mixin = TAG_ATTRIBUTE_MIXINS.get(tag_name.lower())
    return (mixin,) if mixin else tuple()
